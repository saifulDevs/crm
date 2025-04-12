# src/agents/models.py
from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class AgentBase(BaseModel):
    name: str
    department: str
    active: bool = True

class AgentCreate(AgentBase):
    pass

class AgentResponse(AgentBase):
    id: UUID

    class Config:
        orm_mode = True
