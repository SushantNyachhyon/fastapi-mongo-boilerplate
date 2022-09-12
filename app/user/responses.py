"""
user responses
"""
from datetime import datetime
from pydantic import Field, EmailStr
from typing import Optional

from core.models import DocumentFactory


class UserResponse(DocumentFactory):
    """
    user response class
    """

    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False
    last_login: Optional[datetime] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
