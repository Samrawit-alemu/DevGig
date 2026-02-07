from fastapi import APIRouter, HTTPException, status
from typing import List
from beanie import PydanticObjectId # To validate MongoDB IDs

from app.models.job_model import Job
from app.schemas.job_schema import JobCreate, JobResponse, JobUpdate

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

@router.get("/jobs", response_model=List[JobResponse])
async def get_all_jobs():
    # 1. Query the database
    # Job.find_all() prepares the query
    # .to_list() executes it asynchronously
    jobs = await Job.find_all().to_list()
    return jobs

@router.get("/jobs/{job_id}", response_model=JobResponse)
async def get_job_by_id(job_id: PydanticObjectId): # in the parameter chck the id validity
    # 1. search for the job
    job = await Job.get(job_id)

    # 2. Check if it exists
    if not job:
        # If None, return a 404 Error
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    return job

@router.put("/jobs/{job_id}", response_model=JobResponse)
async def update_job(job_id: PydanticObjectId, job_update: JobUpdate):
    # only updates the fields sent by the user

    # 1. Find the job
    job = await Job.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    #2. prepare the update
    # exclude_unset=True means: "If the user didn't send 'budget', don't include it in this dict."
    update_data = job_update.model_dump(exclude_unset=True)

    # 3. Update the database
    # "$set" is a MongoDB command that says "Only change these specific fields"
    await job.update({"$set": update_data})

    return job

@router.delete("jobs/{job_id}")
async def delete_job(job_id:PydanticObjectId):
    # 1 find the job
    job = await Job.get(job_id)
    if not job:
        raise HTTPException(status_code=404, deetail="Job not found")
    
    # 2 delete it
    await job.delete()

    return {"message": "Job deleted successfully"}