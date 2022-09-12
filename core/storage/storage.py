""" utilities for storage """
import os
import uuid
import aiofiles
from pathlib import Path
from datetime import datetime
from fastapi import UploadFile, File
from config import get_settings

settings = get_settings()

BASE_DIR = Path(__file__).resolve().parent.parent
media_path = os.path.join(BASE_DIR, settings.MEDIA_PATH)


async def create_unique_filename() -> str:
    return uuid.uuid4().hex


async def create_or_get_storage_path(storage_path: str) -> dict[str, str]:
    date = datetime.now()
    relative_path = f'{storage_path}/{date.year}/{date.strftime("%m")}'
    path = f"{media_path}/{relative_path}"
    try:
        os.makedirs(path)
    except OSError as ex:
        print(ex)
    return {"relative_path": relative_path, "absolute_path": path}


async def upload(path: str, file: UploadFile = File(...)) -> str:
    filename = os.path.splitext(file.filename)
    unique_name = await create_unique_filename() + filename[1]
    storage_path = await create_or_get_storage_path(path)
    async with aiofiles.open(
        f'{storage_path["absolute_path"]}/{unique_name}', "wb"
    ) as f:
        file_content = await file.read()
        await f.write(file_content)
    return f'{storage_path["relative_path"]}/{unique_name}'
