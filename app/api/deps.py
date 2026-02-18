from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.config import settings
from app.models.user_model import User

# This tells FastAPI: "The token is in the Authorization header, look for 'Bearer <token>'"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# app/api/deps.py

# ... imports ...

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # 1. DEBUG: did we get the token?
    print(f"\n--- DEBUG START ---")
    print(f"Token received: {token[:15]}...") 

    try:
        # 2. DEBUG: Try to decode
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(f"Decoded Payload: {payload}")
        
        email: str = payload.get("sub")
        print(f"Email in token: {email}")
        
        if email is None:
            print("ERROR: No 'sub' (email) found in token.")
            raise credentials_exception

    except JWTError as e:
        # 3. DEBUG: If decoding fails, print WHY
        print(f"JWT DECODE ERROR: {e}")
        raise credentials_exception
    
    # 4. DEBUG: Try to find user in DB
    user = await User.find_one(User.email == email)
    if user is None:
        print(f"ERROR: User with email {email} not found in MongoDB.")
        raise credentials_exception
        
    print("SUCCESS: User found and authorized.")
    print(f"--- DEBUG END ---\n")
    return user