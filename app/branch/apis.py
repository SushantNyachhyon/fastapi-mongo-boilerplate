"""
branch routes
"""
from fastapi import APIRouter
from . import controllers


route = APIRouter(prefix='/branch')

@route.get('')
async def index():
    return await controller.index()
