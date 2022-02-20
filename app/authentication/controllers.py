"""
authentication controllers
"""
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY

from core.security.jwt import create_access_token
from core.security.hash import hash_string, verify_hash

from app.user.requests import UserRequest
from app.user.responses import UserResponse
from app.user.repository import get_user_repo
from .responses import TokenResponse

user_repo = get_user_repo()


async def _check_if_user_exists(user: UserResponse) -> bool:
    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail={
                'username': {
                    'type': 'value_error.invalid',
                    'msg': 'invalid username or password'
                }
            }
        )
    return True


async def _check_if_user_is_active(user: UserResponse) -> bool:
    if not user.is_active:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                'username': {
                    'type': 'value_error.invalid',
                    'msg': 'user is not active'
                }
            }
        )
    return True


async def _verify_password(plain_password: str, hashed_password: str) -> bool:
    if not await verify_hash(plain_password, hashed_password):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail={
                'credentials': {
                    'type': 'value_error.invalid',
                    'msg': 'invalid username or password'
                }
            }
        )
    return True


async def _authenticate(credentials: OAuth2PasswordRequestForm) -> UserResponse:
    user = await user_repo.find_by_email(credentials.username)
    await _check_if_user_exists(user)
    await _check_if_user_is_active(user)
    await _verify_password(credentials.password, user.password)
    return user


async def login(credentials: OAuth2PasswordRequestForm) -> TokenResponse:
    user = await _authenticate(credentials)
    access_token = await create_access_token(data={'id': str(user.id)})
    return TokenResponse(access_token=access_token, token_type='Bearer')


async def register(payload: UserRequest = Body(...)) -> TokenResponse:
    payload.password = await hash_string(payload.password)
    user = await user_repo.create(
        jsonable_encoder(payload)
    )
    access_token = await create_access_token(data={'id': str(user.id)})
    return TokenResponse(access_token=access_token, token_type='Bearer')
