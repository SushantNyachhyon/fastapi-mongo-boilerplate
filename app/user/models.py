"""
user model
"""
from datetime import datetime
from pydantic import EmailStr
from typing import Optional

from core.models import DocumentFactory


class User(DocumentFactory):
    """
    user document class
    """

    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_admin: Optional[bool] = False
    is_active: Optional[bool] = False
    last_login: Optional[datetime] = None
    created: Optional[datetime] = None
