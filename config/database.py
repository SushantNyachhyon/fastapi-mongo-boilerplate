"""
database connection configuration
"""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from .settings import get_settings

settings = get_settings()

database_pool = None


def init_database() -> AsyncIOMotorDatabase:
    global database_pool
    if database_pool is None:
        client = AsyncIOMotorClient(settings.DB_CON_STRING)
        database_pool = client[settings.DB_NAME]
    return database_pool
