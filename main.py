"""
main application module
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from config import database, get_settings
from routes import router


settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    docs_url=None,
    redoc_url=None,
)
app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.mount(
    settings.STATIC_URL,
    StaticFiles(directory=settings.STATIC_PATH),
    name=settings.STATIC_PATH,
)
app.mount(
    settings.MEDIA_URL,
    StaticFiles(directory=settings.MEDIA_PATH),
    name=settings.MEDIA_PATH,
)


# custom validation message
@app.exception_handler(RequestValidationError)
async def validtion_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    errors = {}
    for error in exc.errors():
        errors[error["loc"][1]] = {"type": error["type"], "msg": error["msg"]}

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"errors": errors}),
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"errors": exc.detail}),
    )


@app.on_event("startup")
async def startup():
    database.init_database()


@app.get("/docs", include_in_schema=False)
async def swagger_ui() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "",
        title=app.title + " - Documentation",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"{settings.STATIC_URL}/js/swagger.js",
        swagger_css_url=f"{settings.STATIC_URL}/css/swagger.css",
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
