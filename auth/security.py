# auth/security.py
from passlib.context import CryptContext
pwd = CryptContext(schemes=["bcrypt"])

def hash_password(p): return pwd.hash(p)
def verify_password(p, h): return pwd.verify(p, h)
