"""
Authentication routes
"""
from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordRequestForm

from app.user.schemas import UserInCreate
from .schemas import Token
from . import controllers

route = APIRouter(prefix='/auth')


@route.post('/login', response_model=Token)
async def login(
    credentials: OAuth2PasswordRequestForm = Depends()
) -> Token:
    return await controllers.login(credentials)


@route.post('/register', response_model=Token)
async def register(
    payload: UserInCreate = Body(...)
) -> Token:
    return await controllers.register(payload)
