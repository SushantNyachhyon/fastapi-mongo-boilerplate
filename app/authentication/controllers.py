"""
authentication controllers
"""
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from core.security.jwt import create_access_token
from core.security.hash import hash_string

from app.user.requests import UserRequest
from app.user import repository
from .services import (
    check_if_user_exists,
    check_if_user_is_active,
    verify_password,
    validate_username,
)


async def authenticate(credentials: OAuth2PasswordRequestForm) -> dict:
    user = await repository.find_by_email(credentials.username)
    await check_if_user_exists(user)
    await check_if_user_is_active(user)
    await verify_password(credentials.password, user["password"])
    return user


async def login(credentials: OAuth2PasswordRequestForm) -> dict:
    user = await authenticate(credentials)
    access_token = await create_access_token(data={"id": str(user["_id"])})
    return {"access_token": access_token, "token_type": "Bearer"}


async def register(payload: UserRequest = Body(...)) -> dict:
    await validate_username(payload.email)
    payload.password = await hash_string(payload.password)
    user = await repository.create(jsonable_encoder(payload))
    access_token = await create_access_token(data={"id": str(user["_id"])})
    return {"access_token": access_token, "token_type": "Bearer"}
