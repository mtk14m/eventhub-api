from pydantic import BaseModel
import os

class Settings(BaseModel):
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://eventhub_user:eventhub_password@localhost:5432/eventhub_db",
    )

settings = Settings()
