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
from app.user.models import User
from app.user.schemas import UserInCreate
from .schemas import Token


async def _check_if_user_exists(user: User) -> bool:
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


async def _check_if_user_is_active(user: User) -> bool:
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


async def _verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
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


async def _authenticate(credentials: OAuth2PasswordRequestForm) -> User:
    user = await User.find_one(User.email == credentials.username)
    await _check_if_user_exists(user)
    await _check_if_user_is_active(user)
    await _verify_password(credentials.password, user.password)
    return user


async def login(credentials: OAuth2PasswordRequestForm):
    user = await _authenticate(credentials)
    access_token = await create_access_token(data={'id': str(user.id)})
    return Token(access_token=access_token, token_type='Bearer')


async def register(payload: UserInCreate = Body(...)):
    payload.password = await hash_string(payload.password)
    user = User(**jsonable_encoder(payload))
    await user.create()
    access_token = await create_access_token(data={'id': str(user.id)})
    return Token(access_token=access_token, token_type='Bearer')
