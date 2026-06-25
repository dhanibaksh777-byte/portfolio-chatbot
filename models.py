from sqlalchemy import Column, String, Integer, Text
from database import base

class KnowledgeBase(base):
    __tablename__ = "knowledge_base"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    content = Column(Text)
    embedding = Column(Text)