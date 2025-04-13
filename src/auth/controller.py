from typing import Annotated
from fastapi import APIRouter, Depends, Request
from starlette import status
from . import models, service
from fastapi.security import OAuth2PasswordRequestForm
from src.database.core import DbSession


router = APIRouter(prefix='/auth', tags=['auth'])

@router.post("/login", response_model=models.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DbSession):
    return service.login_for_access_token(form_data, db)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(request: Request, db: DbSession, register_user_request: models.RegisterUserRequest):
    return service.register_user(db, register_user_request)

