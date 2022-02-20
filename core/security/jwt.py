""" jwt utilities """
from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import jwt, JWTError

from config import get_settings

settings = get_settings()

SECRET_KEY = settings.APP_SECRET
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def create_access_token(
    data: dict,
    expiry_time: timedelta | None = None
) -> str:
    encode = data.copy()
    if expiry_time:
        expire = datetime.utcnow() + expiry_time
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def verify_access_token(
    token: str,
    credentials_exception: HTTPException
) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        identifier = payload.get('id')
        if identifier is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception from e
    return identifier
