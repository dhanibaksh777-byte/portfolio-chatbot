from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str

class KnowledgeCreate(BaseModel):
    category: str
    content: str

class KnowledgeOut(BaseModel):
    id : int 
    category: str
    content: str

    class config:
        from_attributes = True



