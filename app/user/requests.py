"""
user requests
"""
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, validator

from core.models import DocumentFactory
from core.validators import required


class UserRequest(DocumentFactory):
    """
    user create request class
    """

    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    is_active: bool | None = False
    created: datetime | None = datetime.now()

    _required = validator(
        "first_name", "last_name", "password", allow_reuse=True, pre=True
    )(required)
