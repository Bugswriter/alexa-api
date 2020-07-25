from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.models.user import User

router = APIRouter()
def get_db():
    db = SessionLocal()
    return db

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/{user_id}")
def read_user(db: Session = Depends(get_db)):
    pass
