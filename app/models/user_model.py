from beanie import Document, Indexed
from pydantic import Field, EmailStr
from datetime import datetime

class User(Document):
    # Indexed(..., unique=True) ensures no two users have the same email
    # EmailStr checks email validity (if it looks like an email)
    email: Indexed(EmailStr, unique=True) # type: ignore
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users" #Collection name