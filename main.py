from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from core.settings import settings
from apps.utils.media import upload_file
from apps.llama import query_engine


# Defining FastAPI instance, adding middlewares

app = FastAPI(
    title="DevDynamos",
    description="Project created for hackathos",
    version="1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORSE_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/upload-file')
async def send_file(file: UploadFile):
    await upload_file(file)
    return {'status': 'ok'}


@app.post('/answer-question')
async def answer_question(question: str):
    responce = query_engine.query(question)
    return {
        'answer': responce.response,
    }
