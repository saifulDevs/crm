# src/agents/service.py
from sqlalchemy.orm import Session
from .entities import Agent
from .models import AgentCreate
import uuid

def create_agent(db: Session, agent_data: AgentCreate):
    agent = Agent(
        id=uuid.uuid4(),
        name=agent_data.name,
        department=agent_data.department,
        active=agent_data.active
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def get_agents(db: Session):
    return db.query(Agent).all()


def get_agent_by_id(agent_id: uuid.UUID, db: Session):
    return db.query(Agent).filter(Agent.id == agent_id).first()