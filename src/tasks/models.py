from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from enum import Enum as PyEnum
from datetime import datetime
from ..database.core import Base


class TaskStatus(PyEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=False)
    due_date = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(TaskStatus), default=TaskStatus.Pending)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    user = relationship('User', back_populates='tasks')

    def __repr__(self):
        return f"<Task(description='{self.description}', status='{self.status}')>"
