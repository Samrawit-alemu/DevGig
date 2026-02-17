from pydantic import BaseModel, EmailStr, Field
from beanie import PydanticObjectId
from datetime import datetime

# 1. Input Schema (What user sends to register/login)
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)

# 2. Output Schema (What we return)
# NOTICE: We do NOT include the password here!
class UserResponse(BaseModel):
    id: PydanticObjectId
    email: EmailStr
    created_at: datetime