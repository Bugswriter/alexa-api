from app.models.spot import Spot
from sqlalchemy.orm import Session
#from app.schemas.spot import SpotCreate as SchemaSpotCreate

class CRUDSpot():
    def get(self, db: Session, spot_id):
        return db.query(Spot).filter(Spot.id == spot_id).first()

    def get_multi(self, db: Session):
        return db.query(Spot).all()

    def get_by_name(self, db: Session, username: str):
        return db.query(Spot).filter(User.name == name).first()

    def create_spot(self, db: Session, user: SchemaUserCreate):
        # fake_hashed_password = user.password + "notreallyhashed"
        # db_user = User(username= user.username, email=user.email, password=fake_hashed_password)
        # db.add(db_user)
        # db.commit()
        # db.refresh(db_user)
        # return db_user

spot = CRUDSpot()
