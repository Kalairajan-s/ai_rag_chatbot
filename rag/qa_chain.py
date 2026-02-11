from langchain_classic.chains import RetrievalQA

from utils.llm import llm
from rag.vectorstore import db
from memory.memory_manager import get_memory

def get_chain(session_id: str, memory_type: str = "buffer"):
    memory = get_memory(session_id, memory_type)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return chain
