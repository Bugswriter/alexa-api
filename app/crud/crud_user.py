from app.models.user import User
from sqlalchemy.orm import Session

class CRUDUser():
    def get(self, db: Session, uid):
        return db.query(User).filter(User.id == uid).first()

    def get_multi(self, db: Session):
        return db.query(User).all()

    def get_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()


user = CRUDUser()
