from fastapi import FastAPI

from eventhub.core.logging import setup_logging
from eventhub.api.events import router as events_router

setup_logging()

app = FastAPI(title="EventHub")

@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}

#Ajoute Event router
app.include_router(events_router)