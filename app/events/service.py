from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4

from fastapi.exceptions import HTTPException
from fastapi import status

from app.celery_worker import create_task

from .schemas import CreateEvent, UpdateEvent, Event

events: List[Event] = []
"""List of events. In-memory storage."""


class EventService:
    """Service for managing events."""

    def get_all(self):
        """Retrieves all events."""
        return events

    def retrieve(self, event_id: UUID):
        """Retrieves a single event by it's id. Raises a 404 if not found."""
        for event in events:
            if event.id != event_id:
                continue

            return event

        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")

    def create(self, payload: CreateEvent):
        """Creates a new event and returns it."""
        defaults = {
            "id": uuid4(),
            "status": "Created",
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }
        event = Event(**defaults, **payload.model_dump())

        user_id = payload.user_id
        event_id = defaults["id"]
        description = payload.description
        create_task.delay(event_id, user_id, description)

        events.append(event)

        return event

    def update(self, event_id: UUID, payload: UpdateEvent):
        """Updates an event and returns it. Raises a 404 if not found."""
        for index, event in enumerate(events):
            if event.id != event_id:
                continue

            updated_event = event.model_copy(
                update=payload.model_dump(exclude_unset=True)
            )
            updated_event.updated_at = datetime.now(timezone.utc)
            events[index] = updated_event

            return updated_event

        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")
