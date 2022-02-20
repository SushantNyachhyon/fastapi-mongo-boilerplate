"""
authentication schemas
"""
from pydantic import BaseModel, Field


class Token(BaseModel):
    """
    token schema class
    """
    access_token: str = Field(...)
    token_type: str = Field(...)
