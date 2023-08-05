import os
import uuid

import PyPDF2
from docx import Document
from fastapi import UploadFile
from fastapi.exceptions import HTTPException


async def upload_file(file: UploadFile) -> str:
    file_extension = file.filename.split(".")[-1]
    if file_extension not in ["pdf", "txt", "docx"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    filename = str(uuid.uuid4())

    with open(f"media/{filename}.{file_extension}", "wb") as f:
        f.write(await file.read())
    return filename


def read_pdf(file):
    with open(file, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        text = ""
        for page in range(reader.getNumPages()):
            text += reader.getPage(page).extractText()
    return text


def read_docx(file):
    document = Document(file)
    text = " ".join([paragraph.text for paragraph in document.paragraphs])
    return text


async def get_text_from_file(file: str) -> str:
    extension = file.split(".")[-1]

    with open(file, "r") as f:
        if extension == "pdf":
            return read_pdf(f)
        elif extension == "docx":
            return read_docx(f)
        else:
            return f.read()


async def read_all_files() -> list:
    text = []

    for file in os.listdir('media/'):
        if os.path.isfile(os.path.join('directory', file)):
            text.append(await get_text_from_file(f"media/{file}"))
    return ' '.join(text)
