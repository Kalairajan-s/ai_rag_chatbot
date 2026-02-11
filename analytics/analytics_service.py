# analytics/analytics_service.py
from sqlalchemy import func
from models import ChatHistory

def most_asked(db):
    return db.query(
        ChatHistory.message,
        func.count(ChatHistory.message)
    ).group_by(ChatHistory.message).all()
