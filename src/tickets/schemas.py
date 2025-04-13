from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from enum import Enum


class TicketStatus(str, Enum):
    Open = "Open"
    InProgress = "InProgress"
    Resolved = "Resolved"
    Closed = "Closed"


class TicketBase(BaseModel):
    subject: str
    description: str
    status: TicketStatus
    due_date: datetime


class TicketCreate(TicketBase):
    pass


class TicketResponse(TicketBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    agent_id: UUID

    class Config:
        orm_mode = True
