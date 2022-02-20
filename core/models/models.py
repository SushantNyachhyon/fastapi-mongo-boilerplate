"""
base model classes
"""
from datetime import datetime
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field


class DocumentFactory(Document):
    """
    base document class for creating collection
    """
    created: datetime | None = None
    updated: datetime | None = None


class SchemaFactory(BaseModel):
    """
    base model class for defining schema
    """
    id: PydanticObjectId = Field(None, alias='_id')
    created: datetime | None = None
    updated: datetime | None = None
