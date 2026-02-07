# The entry point where we turn the key
from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.config import settings
from app.models.job_model import Job # import our 
from app.api.router import router as api_router

# 1. Define the Lifespan (Startup/Shutdown logic)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    print("Starting up ... Connecting to MongoDB")

    #Create the Motor Client (the connection line)
    client = AsyncIOMotorClient(settings.DATABASE_URL)

    # Initialize Beanie( the translator) - we tell it which db to use and which models to watch
    await init_beanie(
        database=client[settings.DATABASE_NAME],
        document_models=[Job]
    )

    print("MongoDB Connected Successfully")

    yield # The app runs while yielded

    # SHUTDOWN
    print("Shutting down...")

#  2. Pass lifespan to fastapi
app = FastAPI(title="DevGig API", version="1.0", lifespan=lifespan)

# Router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def health_check():
    return {"status": "ok", "app_name": "DevGig"}