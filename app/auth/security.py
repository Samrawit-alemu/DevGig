from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt # The library for JWTs
from app.config import settings # To get the secret key

# 1. Setup the context (We use Bcrypt, the industry standard)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

# 2. Function to Hash a password (Registering)
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 3. Function to Verify a password (Logging in)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    
    # Set expiration time
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(days=1) #minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    
    # Add expiration to the data
    to_encode.update({"exp": expire})
    
    # Encode the JWT
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt