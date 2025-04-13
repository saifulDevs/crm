from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID
from datetime import datetime


def create_ticket(db: Session, ticket_request: schemas.TicketCreate) -> models.Ticket:
    new_ticket = models.Ticket(
        subject=ticket_request.subject,
        description=ticket_request.description,
        status=ticket_request.status,
        due_date=ticket_request.due_date,
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


def get_all_tickets(db: Session) -> list[models.Ticket]:
    return db.query(models.Ticket).all()


def get_ticket(db: Session, ticket_id: UUID) -> models.Ticket | None:
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()


def update_ticket(
    db: Session, ticket_id: UUID, ticket_request: schemas.TicketCreate
) -> models.Ticket | None:
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if ticket:
        ticket.subject = ticket_request.subject
        ticket.description = ticket_request.description
        ticket.status = ticket_request.status
        ticket.due_date = ticket_request.due_date
        ticket.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(ticket)
        return ticket
    return None
