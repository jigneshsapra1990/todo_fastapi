from pydantic import BaseModel
from typing import Optional

class QueryParametrs(BaseModel):
    name: Optional[str] = None
    age: int