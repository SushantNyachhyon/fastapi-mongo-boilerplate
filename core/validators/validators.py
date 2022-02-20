""" utilities for validations """
from fastapi import UploadFile, File, HTTPException, status
from typing import List


def required(value: str) -> str:
    if len(value) == 0:
        raise ValueError('field required')
    return value


async def validate_file(
    mimes: List[str],
    file: UploadFile = File(...)
) -> bool:
    if file.content_type in mimes:
        return True
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            'file': {
                'type': 'file_error.invalid',
                'msg': 'not a valid file type'
            }
        }
    )

