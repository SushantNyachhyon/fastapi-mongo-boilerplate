""" utilities for storage """
import os
import uuid
import shutil
import aiofiles
from pathlib import Path
from datetime import datetime
from fastapi import UploadFile, File
from config import get_settings

settings = get_settings()

BASE_DIR = Path(__file__).resolve().parent.parent
media_path = os.path.join(BASE_DIR, settings.MEDIA_PATH)


async def _create_unique_filename() -> str:
    return uuid.uuid4().hex


async def _create_or_get_storage_path(storage_path: str) -> dict:
    date = datetime.now()
    relative_path = f'{storage_path}/{date.year}/{date.strftime("%m")}'
    path = f'{media_path}/{relative_path}'
    try:
        os.makedirs(path)
    except OSError as ex:
        print(ex)
    return {'relative_path': relative_path, 'absolute_path': path}


async def upload(path: str, file: UploadFile = File(...)) -> str:
    filename = os.path.splitext(file.filename)
    unique_name = await _create_unique_filename() + filename[1]
    path = await _create_or_get_storage_path(path)
    async with aiofiles.open(
        f'{path["absolute_path"]}/{unique_name}', 'w'
    ) as f:
        f.write(file.file)
    return f'{path["relative_path"]}/{unique_name}'
