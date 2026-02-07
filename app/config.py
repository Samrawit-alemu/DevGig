# Settings : DB URL, Secrets

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # This define the name of the database we will create in Mongo
    DATABASE_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "devgig_db"

    class Config:
        env_file = ".env"

settings = Settings()