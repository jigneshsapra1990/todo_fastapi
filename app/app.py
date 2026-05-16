from fastapi import FastAPI ,Depends, HTTPException
from typing import Annotated
from type import QueryParametrs
from app.routing import todo
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
from app.config.app_config import AppConfig
load_dotenv()

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = {}
    for error in exc.errors():
        errors[error['loc'][-1]] = error['msg']

    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation Error",
            "errors": errors,
        }
    )
    



app.include_router(todo.router)

