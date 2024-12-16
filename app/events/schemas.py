from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CreateEvent(BaseModel):
    description: str
    user_id: UUID


class UpdateEvent(BaseModel):
    status: Optional[str] = None


class Event(BaseModel):
    id: UUID
    description: str
    status: str
    user_id: UUID
    created_at: datetime
    updated_at: datetime
