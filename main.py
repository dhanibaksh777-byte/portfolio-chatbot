from fastapi import FastAPI
from database import engine 
import models
from chatbot import router as chatbot_router

models.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chatbot_router)