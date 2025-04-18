from datetime import datetime, timedelta, timezone
from uuid import uuid4, UUID
from typing import Annotated
import logging
import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from . import models
from src.entities.user import User
from src.exceptions import AuthenticationError

# You would want to store this in an environment variable or a secret manager
SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)

def authenticate_user(email: str, password: str, db: Session) -> User | bool:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        logging.warning(f"Failed authentication for {email}")
        return False
    return user

def create_access_token(email: str, user_id: UUID, expires_delta: timedelta) -> str:
    to_encode = {
        "sub": email,
        "id": str(user_id),
        "exp": datetime.now(timezone.utc) + expires_delta
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> models.TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get('id')
        return models.TokenData(user_id=user_id)
    except jwt.PyJWTError as e:
        raise AuthenticationError()

def register_user(db: Session, register_user_request: models.RegisterUserRequest):
    user = User(
        id=uuid4(),
        email=register_user_request.email,
        first_name=register_user_request.first_name,
        last_name=register_user_request.last_name,
        password_hash=get_password_hash(register_user_request.password)
    )
    db.add(user)
    db.commit()

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]) -> models.TokenData:
    return verify_token(token)

CurrentUser = Annotated[models.TokenData, Depends(get_current_user)]

def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session) -> models.Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise AuthenticationError()
    token = create_access_token(user.email, user.id, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return models.Token(access_token=token, token_type='bearer')