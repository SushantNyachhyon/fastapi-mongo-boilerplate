"""
user requests
"""
from pydantic import BaseModel, Field, EmailStr


class UserRequest(BaseModel):
    """
    user create request class
    """
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
