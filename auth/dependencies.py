# auth/dependencies.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from config import settings

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token=Depends(oauth2)):
    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
    except:
        raise HTTPException(401, "Invalid token")
