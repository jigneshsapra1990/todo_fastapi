from fastapi import APIRouter,Depends
from typing import Annotated
from type import QueryParametrs
from app.models.todo import CreateTodo


router = APIRouter(prefix="/todo",tags=["Todo"])


@router.post("/")
def addTodo(item: CreateTodo):
    return {"message": f"Hello Fast Api {item}"}

"""Quey Parametrs"""
@router.get("/")
def getPost(params: Annotated[QueryParametrs, Depends()]):
    return {"message": f"Hello Fast Api {params.name} and age is {params.age}"}

@router.get("/{id}")
def root(id:int):
    return {"message": f"Hello Fast Api {id}"}