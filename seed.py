from database import SessionLocal
from models import KnowledgeBase
from database import base, engine

base.metadata.create_all(bind=engine)

db = SessionLocal()

data = [
    {
        "category": "bio",
        "content": "Dhani Baksh is a 17-year-old self-taught backend developer from Pakistan. He learned backend development in just 4 months, completely self-taught with no formal mentorship. He is currently learning AI integration to become an AI Integration Engineer."
    },
    {
        "category": "skills",
        "content": "Backend skills: FastAPI, SQLAlchemy, PostgreSQL, MySQL, JWT authentication, OAuth2PasswordBearer, Alembic migrations, Pydantic schemas, bcrypt password hashing, custom OOP error handling. AI integration skills: Groq API (Llama 3.3 70B), function calling, conversation memory storage, prompt engineering, RAG (Retrieval Augmented Generation)."
    },
    {
        "category": "project",
        "content": "Ecommerce API: A full-stack ecommerce backend built with FastAPI, PostgreSQL (Supabase), and SQLAlchemy. Features include JWT authentication, custom OOP error handling, pagination, and background email tasks using smtplib. Frontend built with Next.js (via V0.dev) and deployed on Vercel, backend deployed on Render."
    },
    {
        "category": "project",
        "content": "Blog API: A backend API built with FastAPI, Supabase Auth, PostgreSQL, and Cloudinary for image storage. Originally planned with a React/Vite frontend but ultimately deployed with a vanilla JavaScript single-file frontend."
    },
    {
        "category": "project",
        "content": "Auth System: One of the foundational projects built early in the learning journey, including a User model, Pydantic schemas, and a complete authentication router using JWT and OAuth2PasswordBearer."
    },
    {
        "category": "project",
        "content": "AI Chatbot (CodeBuddy/Dhani): The first AI integration project, a FastAPI chatbot with a custom persona, built using the Groq API (Llama 3.3 70B). Later extended with function calling and conversation memory storage in PostgreSQL by session_id."
    },
    {
        "category": "project",
        "content": "Portfolio Bot: An AI-powered chatbot for a personal portfolio website that combines RAG (to answer questions using stored personal/project data), function calling (to perform specific actions), and conversation memory storage, built using FastAPI, PostgreSQL, and the Groq API."
    },
    {
        "category": "experience",
        "content": "Worked on the backend for Scaterly, an AI-powered content distribution startup. Built and deployed a production FastAPI REST API using PostgreSQL, SQLAlchemy, JWT authentication, Supabase, and Render for deployment. Collaborated directly with other developers on the team, gaining real-world experience working alongside other devs."
    },
    {
        "category": "github",
        "content": "GitHub profile: https://github.com/dhanibaksh777-byte"
    },
    {
        "category": "goals",
        "content": "Career goal is to work as a Software Engineer, specifically specializing in AI Integration Engineering. Long-term goal is to build his own startups in the future."
    },
]

for item in data:
    entry = KnowledgeBase(**item)
    db.add(entry)

db.commit()
db.close()
print("Data inserted successfully!")