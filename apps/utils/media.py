import os
import uuid

from fastapi import UploadFile
from fastapi.exceptions import HTTPException

from core.settings import settings


async def upload_file(file: UploadFile):
    file_extension = file.filename.split(".")[-1]
    if file_extension not in ('txt',):
        raise HTTPException(
            status_code=400, detail="File extension not allowed")

    file.filename = uuid.uuid4().hex + "." + file_extension

    with open(settings.MEDIA_ROOT / file.filename, "wb") as f:
        f.write(await file.read())
