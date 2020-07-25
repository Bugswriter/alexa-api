from app.models.spot import Spot
from sqlalchemy.orm import Session

class CRUDSpot():
    def get(self, db: Session, spot_id):
        return db.query(Spot).filter(Spot.id == spot_id).first()

    def get_multi(self, db: Session):
        return db.query(Spot).all()

    def get_by_name(self, db: Session, username: str):
        return db.query(Spot).filter(User.name == name).first()

spot = CRUDSpot()
