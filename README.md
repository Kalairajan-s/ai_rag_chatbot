# 🧠 AI RAG Chatbot Backend  
**Memory • Retrieval-Augmented Generation (RAG) • FastAPI • LangChain • Vector DB**

---

## 📌 Project Overview

This project implements an **enterprise-grade backend for a Conversational AI Chatbot** using **FastAPI** and **LangChain**.

The chatbot supports:

- ✅ Session-based conversational memory
- ✅ Retrieval Augmented Generation (RAG) using PDFs
- ✅ Vector search using ChromaDB
- ✅ Source citations with answers
- ✅ Extensible architecture (Auth, Streaming, Tools ready)

---

## 🏗️ Architecture

Client → FastAPI → LangChain (Memory + RAG) → ChromaDB → Documents

---

## 🧰 Tech Stack

- FastAPI  
- LangChain (classic + openai)  
- OpenAI  
- ChromaDB  
- PyPDF  
- Uvicorn  
- Python 3.10+  

---

## 📁 Folder Structure

```
ai_rag_chatbot_backend/
├── app.py
├── config.py
├── database.py
├── models.py
├── auth/
├── memory/
├── rag/
├── tools/
├── analytics/
├── streaming/
├── utils/
├── data/
├── vectorstore/
├── .env
└── README.md
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
CHROMA_PERSIST_DIR=vectorstore
```

---

## ▶️ Step-by-Step Setup

### 1️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```
pip install fastapi uvicorn pydantic python-dotenv langchain langchain-classic langchain-openai langchain-community chromadb pypdf
```

### 3️⃣ Add PDFs

Place PDFs inside:
```
data/
```

### 4️⃣ Ingest Documents

```
python rag/ingest.py
```

### 5️⃣ Run Server

```
uvicorn app:app --reload
```

Open:
```
http://127.0.0.1:8000/docs
```

---

## 🧪 Test API

POST `/chat`

```
{
  "message": "What is RAG?",
  "session_id": "test-1",
  "memory_type": "buffer"
}
```

---
