"""
application routes
"""
from fastapi import APIRouter
from app.authentication.apis import route as auth_routes

router = APIRouter()

router.include_router(auth_routes, prefix="/api/v1", tags=["Authentication"])
