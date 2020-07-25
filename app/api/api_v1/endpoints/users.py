from typing import Optional
from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.crud.crud_user import user as usercrud
from app.schemas.user import UserCreate as SchemaUserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_users(username : Optional[str] = None ,db: Session = Depends(get_db)):
    if username:
        return usercrud.get_by_username(db = db , username= username)
    users = usercrud.get_multi(db)
    return users



@router.post('/registration')
def create_user(*, db : Session = Depends(get_db), user : SchemaUserCreate):
    return usercrud.create_user(db= db, user = user)
    