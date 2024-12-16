from typing import List
from uuid import UUID

from fastapi import APIRouter, status

from .schemas import Event, CreateEvent, UpdateEvent
from .service import EventService

event_router = APIRouter()
event_service = EventService()


# TODO: Delete endpoint, as it isn't part of the requirements.
@event_router.get("", response_model=List[Event])
def get_all_events() -> List[Event]:
    events = event_service.get_all()
    return events


@event_router.post("", status_code=status.HTTP_201_CREATED, response_model=Event)
def create_a_event(
    payload: CreateEvent,
) -> Event:
    event = event_service.create(payload)
    return event


@event_router.get("/{event_id}", response_model=Event)
def retrieve_event(
    event_id: UUID,
) -> Event:
    event = event_service.retrieve(event_id)
    return event


@event_router.patch("/{event_id}", response_model=Event)
def update_event(
    event_id: UUID,
    payload: UpdateEvent,
) -> Event:
    event = event_service.update(event_id, payload)
    return event
