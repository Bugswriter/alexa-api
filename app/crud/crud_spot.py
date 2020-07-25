from app.models.spot import Spot
from sqlalchemy.orm import Session
from app.schemas.spots import SpotCreate as SchemaSpotCreate

class CRUDSpot():
    def get(self, db: Session, spot_id):
        return db.query(Spot).filter(Spot.id == spot_id).first()

    def get_multi(self, db: Session):
        return db.query(Spot).all()

    def get_by_name(self, db: Session, name : str):
        return db.query(Spot).filter(Spot.name == name).first()

    def create_spot(self, db: Session, spot: SchemaSpotCreate):
        db_spot = Spot(name= spot.name, location= spot.location, info= spot.info, special_attraction= spot.special_attraction, thigns_to_do= spot.thigns_to_do, time_to_visit= spot.time_to_visit, near_by_places= spot.near_by_places, similar_places= spot.similar_places, how_to_reach= spot.how_to_reach)
        db.add(db_spot)
        db.commit()
        db.refresh(db_spot)
        return db_spot

spot = CRUDSpot()
