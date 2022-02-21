"""
base model classes
"""
from datetime import datetime
from beanie import (
    Document,
    PydanticObjectId,
    before_event,
    Insert,
    Replace
)
from pydantic import BaseModel, Field
from typing import Optional


class DocumentFactory(Document):
    """
    base document class for creating collection
    """
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    @before_event(Insert)
    def add_created_date(self):
        self.created = datetime.now()

    @before_event(Replace)
    def add_updated_date(self):
        self.updated = datetime.now()


class SchemaFactory(BaseModel):
    """
    base model class for defining schema
    """
    id: PydanticObjectId = Field(None, alias='_id')
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
