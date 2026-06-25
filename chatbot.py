from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from embeddings import get_embedding
from dotenv import load_dotenv
from models import KnowledgeBase
from database import get_db
from groq import Groq
import schemas
import os 
import json
import numpy as np


load_dotenv()

client = Groq(api_key=os.getenv("Groq_api"))

router = APIRouter()


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


@router.post("/chat")
def chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):

    # 1. user query embedding
    query_embedding = get_embedding(request.message)

    # 2. fetch knowledge base
    all_knowledge = db.query(KnowledgeBase).all()

    best_match = None
    best_score = 0.0

    for row in all_knowledge:

        if not row.embedding:
            continue

        try:
            stored_embedding = json.loads(row.embedding)
        except Exception:
            continue

        score = cosine_similarity(query_embedding, stored_embedding)

        if score > best_score:
            best_score = score
            best_match = row

    # 3. IMPORTANT FIX: no fake “no context” text
    context = best_match.content if best_match else ""

    # 4. LLM call
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a portfolio assistant for Dhani Baksh. "
                    "If context is provided, use it. "
                    "If context is empty, answer generally and do not make up facts.\n\n"
                    f"Context:\n{context}"
                )
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "reply": response.choices[0].message.content,
        "best_score": best_score
    }