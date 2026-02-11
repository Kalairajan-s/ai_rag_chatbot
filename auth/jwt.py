# auth/jwt.py
from jose import jwt
from datetime import datetime, timedelta
from config import settings

def create_token(data):
    data["exp"] = datetime.utcnow() + timedelta(
        hours=settings.JWT_EXPIRE_HOURS
    )
    return jwt.encode(
        data,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
