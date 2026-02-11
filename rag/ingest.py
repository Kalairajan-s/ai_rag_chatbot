from langchain_community.document_loaders import PyPDFLoader
from rag.vectorstore import db

# Load PDF documents
loader = PyPDFLoader("data/SD0109_Chatbots.pdf")
docs = loader.load()

# Store documents in ChromaDB
db.add_documents(docs)
db.persist()

print("✅ Documents ingested successfully into ChromaDB")
