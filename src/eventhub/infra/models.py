from datetime import datetime
from typing import Any
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, JSON, Index, text

class Base(DeclarativeBase):
    pass

class Event(Base):
    __tablename__="events"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[str] = mapped_column(String(100), index=True)
    source: Mapped[str] = mapped_column(String(100), index=True)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("now()"),
        index=True
    )

Index("ix_events_type_created", Event.event_type, Event.created_at)