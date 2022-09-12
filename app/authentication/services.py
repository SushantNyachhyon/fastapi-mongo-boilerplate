"""
user services
"""
from core.security.hash import verify_hash
from app.user import repository
from app.user.responses import UserResponse
from utils.exceptions import unprocessable, not_found


async def check_if_user_exists(user: dict) -> bool:
    if not user:
        raise not_found("username", msg="invalid email or password")
    return True


async def check_if_user_is_active(user: dict) -> bool:
    if not user["is_active"]:
        raise unprocessable("username", msg="user is not active")
    return True


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not await verify_hash(plain_password, hashed_password):
        raise not_found("username", msg="invalid email or password")
    return True


async def validate_username(email: str) -> bool:
    data = await repository.find_by_email(email)
    if data is not None:
        raise unprocessable("username", "user already exists")
    return True
