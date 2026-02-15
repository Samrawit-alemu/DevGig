from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserCreate, UserResponse
from app.models.user_model import User
from app.auth.security import get_password_hash

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_input: UserCreate):
    """
    Register a new user with email and password.
    """
    # 1. Check if email already exists
    # We query the User collection looking for this email
    user_exists = await User.find_one(User.email == user_input.email)
    
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # 2. Hash the password
    # We never save the plain text password!
    hashed_pass = get_password_hash(user_input.password)
    
    # 3. Create the User Document
    new_user = User(
        email=user_input.email,
        hashed_password=hashed_pass
    )
    
    # 4. Save to MongoDB
    await new_user.create()
    
    # 5. Return the user (FastAPI filters out the password based on UserResponse)
    return new_user