"""
user schemas
"""
from pydantic import BaseModel, Field, EmailStr


class UserInCreate(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
