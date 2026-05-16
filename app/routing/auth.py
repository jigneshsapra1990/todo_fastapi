from fastapi import APIRouter, Depends, Header
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.auth import Register, Login
from app.controller import auth as auth_controller

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(data: Register, db: Annotated[Session, Depends(get_db)]):
    return auth_controller.register(data, db)


@router.post("/login")
def login(data: Login, db: Annotated[Session, Depends(get_db)]):
    return auth_controller.user_login(data, db)


@router.get("/me")
def is_authenticated(db: Annotated[Session, Depends(get_db)], authorization: Annotated[str, Header()]):
    return auth_controller.is_authenticated(authorization, db)
