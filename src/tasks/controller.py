from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from . import models, schemas, service
from ..database.core import get_db
from ..rate_limiter import limiter

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("/", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
# @limiter.limit("10/minute")
async def create_task(
    task_request: schemas.TaskCreate, db: Session = Depends(get_db)
):
    task = service.create_task(db=db, task_request=task_request)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task creation failed")
    return task


@router.get("/", response_model=list[schemas.TaskResponse])
async def get_all_tasks(db: Session = Depends(get_db)):
    tasks = service.get_all_tasks(db=db)
    return tasks


@router.get("/{task_id}", response_model=schemas.TaskResponse)
async def get_task(task_id: UUID, db: Session = Depends(get_db)):
    task = service.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=schemas.TaskResponse)
async def update_task(
    task_id: UUID, task_request: schemas.TaskCreate, db: Session = Depends(get_db)
):
    task = service.update_task(db=db, task_id=task_id, task_request=task_request)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
