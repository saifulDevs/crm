from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID
from datetime import datetime


def create_task(db: Session, task_request: schemas.TaskCreate) -> models.Task:
    new_task = models.Task(
        description=task_request.description,
        due_date=task_request.due_date,
        status=task_request.status,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_all_tasks(db: Session) -> list[models.Task]:
    return db.query(models.Task).all()


def get_task(db: Session, task_id: UUID) -> models.Task | None:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(
    db: Session, task_id: UUID, task_request: schemas.TaskCreate
) -> models.Task | None:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.description = task_request.description
        task.due_date = task_request.due_date
        task.status = task_request.status
        task.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(task)
        return task
    return None
