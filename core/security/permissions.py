"""
permissions and access
"""
from fastapi import Depends

from .oauth import is_authenticated
from config import init_database
from utils.exceptions import forbidden, unauthorized


async def is_active_user(verified_id: str = Depends(is_authenticated)):
    db = init_database()["users"]
    user = await db.find_one({"_id": verified_id})
    if not user["is_active"]:
        raise unauthorized(identifier="user", msg="user is not active")
    return user


async def is_admin(user: dict = Depends(is_active_user)):
    if not user["is_admin"]:
        raise forbidden(identifier="user")
    return user
