"""
base model classes
"""
from datetime import datetime
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from typing import Optional


class DocumentFactory(Document):
    """
    base document class for creating collection
    """
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class SchemaFactory(BaseModel):
    """
    base model class for defining schema
    """
    id: PydanticObjectId = Field(None, alias='_id')
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
