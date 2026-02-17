from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user_schema import UserCreate, UserResponse
from app.models.user_model import User
from app.auth.security import get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

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


@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    # 1. Find the user (form_data.username contains the email)
    user = await User.find_one(User.email == form_data.username)
    
    # 2. Check if user exists AND password is correct
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Create the token
    access_token = create_access_token(data={"sub": user.email})
    
    # 4. Return the token
    return {"access_token": access_token, "token_type": "bearer"}