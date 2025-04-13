from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from enum import Enum as PyEnum
from datetime import datetime
from ..database.core import Base


class TicketStatus(PyEnum):
    Open = "Open"
    InProgress = "InProgress"
    Resolved = "Resolved"
    Closed = "Closed"


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TicketStatus), default=TicketStatus.Open)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    due_date = Column(DateTime, default=datetime.utcnow)
    agent_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    agent = relationship('User', back_populates='assigned_tickets')

    def __repr__(self):
        return f"<Ticket(subject='{self.subject}', status='{self.status}')>"
