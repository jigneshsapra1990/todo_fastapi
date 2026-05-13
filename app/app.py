from fastapi import FastAPI ,Depends, HTTPException
from typing import Annotated
from type import QueryParametrs
from app.routing import todo
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = {}
    for error in exc.errors():
       errors[error['loc'][-1]] = error['msg']


       return JSONResponse(
           {
               "message": "Validation Error",
               "errors": errors,  
               "status_code": 422 ,
           }
       )
    



app.include_router(todo.router)

