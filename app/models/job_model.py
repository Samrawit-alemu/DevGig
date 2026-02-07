from beanie import Document
from datetime import datetime
from pydantic import Field
from typing import List

class Job(Document): # Inheriting from Doc tells Beanie " this class represents a document in MongoDB"
    title: str
    description: str
    budget: float
    skills: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now) # if date is not given put the current time

    class Settings:
        # This is the collection name in MongoDB
        name = "jobs"