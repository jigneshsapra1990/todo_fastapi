from sqlalchemy import Column, Integer, String, Boolean, VARCHAR,DATETIME
from app.database.db import Base
from datetime import datetime, timezone

class TodoSchema(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(VARCHAR(200), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    crreated_at = Column(DATETIME, nullable=False, default=datetime.now(
        timezone.utc))
    updated_at = Column(DATETIME, nullable=False, default=datetime.now(
        timezone.utc))


