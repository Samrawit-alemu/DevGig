from beanie import PydanticObjectId
from datetime import datetime
from pydantic import Field, BaseModel
from typing import List, Optional

# 1. Base Schema (Shared properties)
class JobBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=50) #... means required
    description: str = Field(..., min_length=10)
    budget: float = Field(..., gt=0)
    skills: List[str] = [] # default empty list

# 2. Schema for creating a job (input)
# This is what the user sends via POST
class JobCreate(JobBase):
    pass

# 3. Schema for reading a job (output)
# This is what we return to the user. It includes the ID and Date.
class JobResponse(JobBase):
    id: PydanticObjectId
    created_at: datetime

    class Config:
        # this is pydantic to treat the beanie document as a dict
        from_attribute = True

class JobUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, min_length=10)
    budget: Optional[float] = Field(None, gt=0)
    skills: Optional[List[str]] = None