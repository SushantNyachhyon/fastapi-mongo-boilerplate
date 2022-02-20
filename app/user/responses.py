"""
user responses
"""
from datetime import datetime
from pydantic import Field, EmailStr
from typing import Optional

from core.models import SchemaFactory


class UserResponse(SchemaFactory):
    """
    user response class
    """
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    is_active: Optional[datetime] = None
    last_login: Optional[datetime] = None
