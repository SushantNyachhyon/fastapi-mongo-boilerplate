"""
application routes
"""
from fastapi import APIRouter
from app.authentication.api import route as _auth_routes

router = APIRouter()

router.include_router(_auth_routes, tags=['Authentication'])
