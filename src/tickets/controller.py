from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from . import models, schemas, service
from ..database.core import get_db


router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)



@router.post("/", response_model=schemas.TicketResponse, status_code=status.HTTP_201_CREATED)
async def create_ticket(
    ticket_request: schemas.TicketCreate, db: Session = Depends(get_db)
):
    ticket = service.create_ticket(db=db, ticket_request=ticket_request)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ticket creation failed")
    return ticket


@router.get("/", response_model=list[schemas.TicketResponse])
async def get_all_tickets(db: Session = Depends(get_db)):
    tickets = service.get_all_tickets(db=db)
    return tickets


@router.get("/{ticket_id}", response_model=schemas.TicketResponse)
async def get_ticket(ticket_id: UUID, db: Session = Depends(get_db)):
    ticket = service.get_ticket(db=db, ticket_id=ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return ticket


@router.put("/{ticket_id}", response_model=schemas.TicketResponse)
async def update_ticket(
    ticket_id: UUID, ticket_request: schemas.TicketCreate, db: Session = Depends(get_db)
):
    ticket = service.update_ticket(db=db, ticket_id=ticket_id, ticket_request=ticket_request)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return ticket
