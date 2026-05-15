from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.todo import CreateTodo
from app.controller import todo as todo_controller

router = APIRouter(prefix="/todo", tags=["Todo"])


@router.get("/")
def get_todos(db: Annotated[Session, Depends(get_db)]):
    return todo_controller.get_all_todos(db)


@router.get("/{id}")
def get_todo(id: int, db: Annotated[Session, Depends(get_db)]):
    return todo_controller.get_todo_by_id(id, db)


@router.post("/")
def add_todo(item: CreateTodo, db: Annotated[Session, Depends(get_db)]):
    return todo_controller.create_todo(item, db)


@router.put("/{id}")
def update_todo(id: int, item: CreateTodo, db: Annotated[Session, Depends(get_db)]):
    return todo_controller.update_todo(id, item, db)


@router.delete("/{id}")
def delete_todo(id: int, db: Annotated[Session, Depends(get_db)]):
    return todo_controller.delete_todo(id, db)
