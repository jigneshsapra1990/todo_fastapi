from fastapi import APIRouter, Depends
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
    return auth_controller.login(data, db)
