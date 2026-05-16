from sqlalchemy.orm import Session
from fastapi import HTTPException
import bcrypt
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.database.schema.user_schema import UserSchema
from app.models.auth import Register, Login
from app.config.app_config import getAppConfig

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())


def create_access_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(payload, getAppConfig().secret_key, algorithm=ALGORITHM)


def register(data: Register, db: Session):
    existing = db.query(UserSchema).filter(UserSchema.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = UserSchema(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token({"sub": str(user.id), "email": user.email})
    return {
        "message": "User registered successfully",
        "data": {"id": user.id, "name": user.name, "email": user.email, "access_token": f"Bearer {token}"}
    }


def login(data: Login, db: Session):
    user = db.query(UserSchema).filter(UserSchema.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token({"sub": str(user.id), "email": user.email})
    return {
        "message": "Login successful",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "access_token": f"Bearer {token}"
        }
    }
