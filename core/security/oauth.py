"""
oauth utilities
"""
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from .jwt import verify_access_token

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl='api/v1/auth/login')


async def is_authenticated(token: str = Depends(OAUTH2_SCHEME)) -> str:
    exception_body = {
        'authentication': {
            'type': 'auth_error.invalid',
            'msg': 'could not validate credentials'
        }
    }
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail=exception_body,
        headers={'WWW-Authenticate': 'Bearer'}
    )
    return await verify_access_token(token, credentials_exception)
