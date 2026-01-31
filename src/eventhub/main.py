from fastapi import FastAPI

from eventhub.core.logging import setup_logging

setup_logging()

app = FastAPI(title="EventHub")

@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
