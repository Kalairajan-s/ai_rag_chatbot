from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import settings

# Create embedding function
embedding = OpenAIEmbeddings(
    api_key=settings.OPENAI_API_KEY
)

# Persistent ChromaDB instance
db = Chroma(
    persist_directory=settings.CHROMA_PERSIST_DIR,
    embedding_function=embedding
)
