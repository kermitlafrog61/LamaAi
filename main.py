from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from core.settings import settings
from apps.bot.bot import StatefulChatbot
from apps.utils.media import upload_file


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

# Creating BOT instance

bot = StatefulChatbot()

@app.post('question/')
async def answer(question: str):
    return {'answer': bot.answer_question(question)}


@app.post('upload-file/')
async def upload_file(file: UploadFile):
    await upload_file(file)
