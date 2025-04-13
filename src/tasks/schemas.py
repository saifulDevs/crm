from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from enum import Enum


class TaskStatus(str, Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"


class TaskBase(BaseModel):
    description: str
    due_date: datetime
    status: TaskStatus


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
