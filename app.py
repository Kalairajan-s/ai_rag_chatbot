from fastapi import FastAPI
from pydantic import BaseModel

from rag.qa_chain import get_chain

app = FastAPI(title="AI RAG Chatbot Backend")


class ChatRequest(BaseModel):
    message: str
    session_id: str
    memory_type: str = "buffer"


@app.post("/chat")
def chat(request: ChatRequest):
    chain = get_chain(
        session_id=request.session_id,
        memory_type=request.memory_type
    )

    response = chain.invoke({
        "query": request.message
    })

    return {
        "session_id": request.session_id,
        "reply": response["result"],
        "sources": [
            doc.metadata for doc in response.get("source_documents", [])
        ]
    }



@app.get("/")
def health():
    return {"status": "running"}
