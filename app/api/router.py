from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models.job_model import Job
from app.schemas.job_schema import JobCreate, JobResponse

# Create a router instance. We will attach this to main.py later.
router = APIRouter()

@router.post("/jobs", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
async def create_job(job_input: JobCreate):
    # Create a new job posting.
     # 1. Convert Pydantic Schema -> Beanie Document
    # We use **job_input.dict() to unpack the data (title, budget, etc.)

    new_job = Job(**job_input.model_dump())

     # 2. Save to MongoDB (Async)
    await new_job.create()

    # 3. Return the created job (FastAPI converts it to JobResponse automatically)
    return new_job