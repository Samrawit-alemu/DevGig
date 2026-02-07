# The entry point where we turn the key
from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="DevGig API", version="1.0")

@app.get("/")
async def health_check():
    return {"status": "ok", "app_name": "DevGig"}