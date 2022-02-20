"""
application routes
"""
from fastapi import APIRouter
from app.authentication.apis import route as _auth_routes

router = APIRouter()

router.include_router(_auth_routes, prefix='/api/v1', tags=['Authentication'])
