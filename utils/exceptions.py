""" utilities for exception handling """
from fastapi.exceptions import HTTPException
from starlette.status import (
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN,
    HTTP_401_UNAUTHORIZED,
)
from typing import Optional


def unprocessable(
    identifier: str, msg: str, exc_type: Optional[str] = "value_error.unprocessable"
) -> HTTPException:
    return HTTPException(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        detail={identifier: {"type": exc_type, "msg": msg}},
    )


def not_found(
    identifier: str,
    msg: Optional[str] = "resource not found",
    exc_type: Optional[str] = "value_error.not_found",
) -> HTTPException:
    return HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail={identifier: {"type": exc_type, "msg": msg}},
    )


def forbidden(
    identifier: str,
    msg: Optional[str] = "you do not have sufficient privilege",
    exc_type: Optional[str] = "value_error.forbidden",
) -> HTTPException:
    return HTTPException(
        status_code=HTTP_403_FORBIDDEN,
        detail={identifier: {"type": exc_type, "msg": msg}},
    )


def unauthorized(
    identifier: str,
    msg: Optional[str] = "you are not authoriezed",
    exc_type: Optional["str"] = "value_error.unauthorized",
):
    return HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={identifier: {"type": exc_type, "msg": msg}},
    )
