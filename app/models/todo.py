from pydantic import BaseModel, Field
from typing import Optional

class CreateTodo(BaseModel):
    title: str = Field(..., min_length=3, max_length=10)
    description: Optional[str] = None
    isCompleted: bool = False