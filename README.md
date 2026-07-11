# AI Portfolio Chatbot (RAG)

A full-stack AI chatbot that answers questions about my portfolio and experience, powered by a custom Retrieval-Augmented Generation (RAG) pipeline.

🔗 **Live Demo:** https://portfolio-chatbot-interface.vercel.app/

## Features

- Retrieval-Augmented Generation pipeline built from scratch (no LangChain)
- Semantic search via cosine similarity over embedded portfolio content
- Fast, context-aware responses using Groq's Llama 3.3 70B
- Lightweight embedding pipeline optimized to run within limited server memory
- Clean, responsive chat interface

## Tech Stack

- **Backend:** FastAPI (Python)
- **LLM:** Groq API (Llama 3.3 70B)
- **Embeddings:** HuggingFace Inference API (`sentence-transformers/all-MiniLM-L6-v2`)
- **Similarity Search:** Cosine similarity (custom implementation)
- **Frontend:** v0.dev generated UI
- **Deployment:** Render (backend) + Vercel (frontend)

## Why HuggingFace Inference API for Embeddings?

Running `sentence-transformers` locally requires loading the full model into memory, which exceeds Render's free-tier 512MB RAM limit. Using HuggingFace's hosted Inference API keeps the backend lightweight while still providing high-quality embeddings.

## Getting Started

### Prerequisites

- Python 3.10+
- Groq API key
- HuggingFace API token

### Installation

```bash
git clone <repo-url>
cd portfolio-chatbot
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file with:

```
groq_api_key=your_groq_api_key
huggingface_api_key=your_hf_api_key
```

### Run Locally

```bash
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| POST | `/chat` | Send a message and get an AI response grounded in portfolio data |
| GET | `/health` | Health check endpoint |

## How It Works

1. Portfolio content is chunked and embedded via HuggingFace's Inference API.
2. On each user query, the query is embedded and compared against stored chunks using cosine similarity.
3. The most relevant chunks are injected into the prompt as context.
4. Groq's Llama 3.3 70B generates a grounded, context-aware response.

## Author

Built by Dhani Baksh — [GitHub](https://github.com/dhanibaksh777-byte)
