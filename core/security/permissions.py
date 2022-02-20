"""
permissions and access
"""
from fastapi import Depends, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from app.user.models import User
from .oauth import is_authenticated


async def is_active_user(verified_id: str = Depends(is_authenticated)):
    user = await User.get(verified_id)
    if not user.is_active:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail={
                'unauthorized': {
                    'type': 'forbidden',
                    'msg': 'user is not active'
                }
            }
        )
    return user


async def is_admin(verified_id: str = Depends(is_authenticated)):
    user = await User.get(verified_id)
    if not user.is_admin:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail={
                'unauthorized': {
                    'type': 'forbidden',
                    'msg': 'you donot have sufficient permission'
                }
            }
        )
    return user

