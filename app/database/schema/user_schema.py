from sqlalchemy import Column, Integer, String, VARCHAR, DateTime
from app.database.db import Base
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column

class UserSchema(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)

    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)

    email: Mapped[str] = mapped_column(VARCHAR(191), nullable=False, unique=True)

    password: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )