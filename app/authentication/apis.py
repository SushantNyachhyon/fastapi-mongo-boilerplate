"""
Authentication routes
"""
from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordRequestForm

from core.security.permissions import is_active_user
from app.user.requests import UserRequest
from app.user.responses import UserResponse
from .responses import TokenResponse
from . import controllers

route = APIRouter(prefix='/auth')


@route.post('/login', response_model=TokenResponse)
async def login(
    credentials: OAuth2PasswordRequestForm = Depends()
) -> TokenResponse:
    return await controllers.login(credentials)


@route.post('/register', response_model=TokenResponse)
async def register(
    payload: UserRequest = Body(...)
) -> TokenResponse:
    return await controllers.register(payload)


@route.get('/me', response_model=UserResponse)
async def get_auth_user(
    user: UserResponse = Depends(is_active_user)
):
    return user
