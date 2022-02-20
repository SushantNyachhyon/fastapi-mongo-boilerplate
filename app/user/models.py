""" user model """
from datetime import datetime
from pydantic import EmailStr
from typing import Optional

from core.models import DocumentFactory


class User(DocumentFactory):
    """ user document class """
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = False
    last_login: datetime | None = None

    class Collection:
        name = 'users'
