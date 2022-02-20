"""
application base settings
"""
from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    setting class to expose the properties
    """
    APP_NAME: str = Field(..., env='APP_NAME')
    APP_DESCRIPTION: str = Field(..., env='APP_DESCRIPTION')
    APP_VERSION: str = Field(..., env='APP_VERSION')
    APP_SECRET: str = Field(..., env='APP_SECRET')
    STATIC_URL: str = Field(..., env='STATIC_URL')
    STATIC_PATH: str = Field(..., env='STATIC_PATH')
    MEDIA_URL: str = Field(..., env='MEDIA_URL')
    MEDIA_PATH: str = Field(..., env='MEDIA_PATH')
    DB_NAME: str = Field(..., env='DB_NAME')
    DB_CON_STRING: str = Field(..., env='DB_CON_STRING')

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
