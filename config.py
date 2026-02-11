import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # ===============================
    # APPLICATION
    # ===============================
    APP_NAME: str = os.getenv("APP_NAME", "AI_RAG_CHATBOT")
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    # ===============================
    # OPENAI
    # ===============================
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # ===============================
    # JWT AUTH
    # ===============================
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRE_HOURS: int = int(os.getenv("JWT_EXPIRE_HOURS", "6"))

    # ===============================
    # POSTGRESQL
    # ===============================
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    # ===============================
    # CHROMADB
    # ===============================
    CHROMA_PERSIST_DIR: str = os.getenv(
        "CHROMA_PERSIST_DIR", "vectorstore/chroma"
    )

    # ===============================
    # VALIDATION (FAIL FAST)
    # ===============================
    def validate(self):
        required = [
            "OPENAI_API_KEY",
            "JWT_SECRET_KEY",
            "POSTGRES_USER",
            "POSTGRES_PASSWORD",
            "POSTGRES_DB"
        ]
        missing = [
            var for var in required if not getattr(self, var)
        ]
        if missing:
            raise RuntimeError(
                f"Missing required env vars: {', '.join(missing)}"
            )

# Instantiate settings
settings = Settings()
settings.validate()
