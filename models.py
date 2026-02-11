from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# ===============================
# USER MODEL
# ===============================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50), default="USER", nullable=False)

    # Relationship
    chats = relationship("ChatHistory", back_populates="user")

    def __repr__(self):
        return f"<User(email={self.email}, role={self.role})>"


# ===============================
# CHAT HISTORY MODEL
# ===============================
class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    session_id = Column(String(100), index=True)
    role = Column(String(20), nullable=False)  # user | bot
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship
    user = relationship("User", back_populates="chats")

    def __repr__(self):
        return f"<ChatHistory(user_id={self.user_id}, role={self.role})>"
