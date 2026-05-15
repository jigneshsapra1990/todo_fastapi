from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DateTime
from app.database.db import Base
from datetime import datetime, timezone


class TodoSchema(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    title = Column(VARCHAR(200), nullable=False)

    description = Column(String, nullable=True)

    completed = Column(Boolean, default=False, nullable=False)

    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )