from datetime import datetime
from typing import Any
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field
from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from eventhub.core.db import get_db_session
from eventhub.infra.models import Event

router = APIRouter(prefix="/events", tags=["events"])

class EventCreate(BaseModel):
    event_type: str = Field(min_length=1, max_length=100)
    source: str = Field(min_length=1, max_length=100)
    payload: dict[str, Any]

class EventOut(BaseModel):
    id: int
    event_type: str
    source: str
    payload: dict[str, Any]
    created_at: datetime

    class Config: 
        from_attributes = True

@router.post("", response_model=EventOut, status_code=201)
async def create_event(
        body: EventCreate,
        db: AsyncSession = Depends(get_db_session)
) -> EventOut:
    ev = Event(event_type=body.event_type, source=body.source, payload=body.payload)
    db.add(ev)
    await db.commit()
    await db.refresh(ev)
    return ev

@router.get("", response_model=list[EventOut])
async def list_events(
    limit: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db_session)
) -> list[EventOut]:
    stmt = select(Event).order_by(Event.created_at.desc()).limit(limit)
    res = await db.execute(stmt)
    return list(res.scalars().all())
    
