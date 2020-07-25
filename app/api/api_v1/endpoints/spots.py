from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.crud.crud_spot import spot as spotcrud

router = APIRouter()

def get_db():
    db = SessionLocal()
    return db

@router.get("/")
def read_spots(db: Session = Depends(get_db)):
    spots = spotcrud.get_multi(db)
    return spots



@router.get("/{spot_id}")
def read_spot(spot_id: int, db: Session = Depends(get_db)):
    spot = spotcrud.get(db, spot_id)
    return spot
