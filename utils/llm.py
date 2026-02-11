from langchain_openai import OpenAI
from config import settings

llm = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    temperature=0.0,
    max_tokens=512
)
