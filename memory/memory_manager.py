from langchain_classic.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory
)
from utils.llm import llm

_store = {}

def get_memory(session_id, memory_type):
    if session_id not in _store:
        _store[session_id] = (
            ConversationSummaryMemory(llm=llm, return_messages=True)
            if memory_type == "summary"
            else ConversationBufferMemory(return_messages=True)
        )
    return _store[session_id]
