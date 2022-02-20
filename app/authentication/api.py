"""
Authentication routes
"""
from fastapi import APIRouter

route = APIRouter(prefix='/auth')


@route.get('/login')
async def login():
    return {'res': 'logged In'}
