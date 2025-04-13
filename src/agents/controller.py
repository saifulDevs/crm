# src/agents/controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from . import service, models
from ..database.core import get_db

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("/", response_model=models.AgentResponse)
def create_agent(agent: models.AgentCreate, db: Session = Depends(get_db)):
    return service.create_agent(db, agent)


@router.get("/", response_model=list[models.AgentResponse])
def list_agents(db: Session = Depends(get_db)):
    return service.get_agents(db)


@router.get("/{agent_id}", response_model=models.AgentResponse)
def read_agent(agent_id: UUID, db: Session = Depends(get_db)):
    db_agent = service.get_agent_by_id(agent_id, db)
    if not db_agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent