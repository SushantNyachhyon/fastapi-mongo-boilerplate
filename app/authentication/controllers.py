"""
authentication controllers
"""
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from core.security.jwt import create_access_token
from core.security.hash import hash_string

from app.user.requests import UserRequest
from app.user.responses import UserResponse
from app.user.repository import get_user_repo
from .responses import TokenResponse
from .services import (
    check_if_user_exists,
    check_if_user_is_active,
    verify_password,
    validate_username
)

user_repo = get_user_repo()


async def _authenticate(credentials: OAuth2PasswordRequestForm) -> UserResponse:
    user = await user_repo.find_by_email(credentials.username)
    await check_if_user_exists(user)
    await check_if_user_is_active(user)
    await verify_password(credentials.password, user.password)
    return user


async def login(credentials: OAuth2PasswordRequestForm) -> TokenResponse:
    user = await _authenticate(credentials)
    access_token = await create_access_token(data={'id': str(user.id)})
    return TokenResponse(access_token=access_token, token_type='Bearer')


async def register(payload: UserRequest = Body(...)) -> TokenResponse:
    await validate_username(payload.username)
    payload.password = await hash_string(payload.password)
    user = await user_repo.create(
        jsonable_encoder(payload)
    )
    access_token = await create_access_token(data={'id': str(user.id)})
    return TokenResponse(access_token=access_token, token_type='Bearer')
