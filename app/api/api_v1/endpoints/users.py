from typing import Optional
from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.crud.crud_user import user as usercrud

router = APIRouter()
def get_db():
    db = SessionLocal()
    return db

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    users = usercrud.get_multi(db)
    return users

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    users = usercrud.get_multi(db)
    return users



@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = usercrud.get(db, user_id)
    return user

