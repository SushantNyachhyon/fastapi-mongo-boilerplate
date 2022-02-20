"""
database connection configuration
"""
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.user.models import User

from .settings import get_settings

settings = get_settings()


async def init_database() -> None:
    client = AsyncIOMotorClient(settings.DB_CON_STRING)
    await init_beanie(
        database=client[settings.DB_NAME],
        document_models=[
            User
        ]
    )
