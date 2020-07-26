from fastapi import APIRouter, Depends
from typing import Optional
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.crud.crud_spot import spot as spotcrud
from app.schemas.spots import SpotCreate as SchemaSpotCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    return db

@router.get("/")
def read_spots(name : Optional[str] = None,db: Session = Depends(get_db)):
    if name:
        return spotcrud.get_by_name(db=db, name = name )
    spots = spotcrud.get_multi(db)
    return spots



@router.get("/{spot_id}")
def read_spot(spot_id: int, db: Session = Depends(get_db)):
    spot = spotcrud.get(db, spot_id)
    return spot

@router.post("/")
def create_spot(*, db : Session = Depends(get_db), spot : SchemaSpotCreate):
    return spotcrud.create_spot(db= db, spot = spot)
