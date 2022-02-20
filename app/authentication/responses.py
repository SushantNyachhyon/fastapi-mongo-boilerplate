"""
authentication responses
"""
from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    """
    token response class
    """
    access_token: str = Field(...)
    token_type: str = Field(...)

