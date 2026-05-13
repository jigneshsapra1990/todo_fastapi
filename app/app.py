from fastapi import FastAPI ,Depends
from typing import Annotated
from type import QueryParametrs

app = FastAPI()

@app.post("/todo")
def addPost(item: dict):
    return {"message": f"Hello Fast Api {item}"}

@app.get("/{id}")
def root(id:int):
    return {"message": f"Hello Fast Api {id}"}

"""Quey Parametrs"""
@app.get("/")
def getPost(params: Annotated[QueryParametrs, Depends()]):
    return {"message": f"Hello Fast Api {params.name} and age is {params.age}"}
