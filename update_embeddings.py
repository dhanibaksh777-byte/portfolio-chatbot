from database import SessionLocal
from models import KnowledgeBase
from embeddings import get_embedding
import json

db = SessionLocal()

all_rows = db.query(KnowledgeBase).all()

for row in all_rows:
    embedding = get_embedding(row.content)
    row.embedding = json.dumps(embedding)

db.commit()
db.close()

print("Embeddings updated successfully!")