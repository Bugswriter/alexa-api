from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate as SchemaUserCreate

class CRUDUser():
    def get(self, db: Session, uid):
        return db.query(User).filter(User.id == uid).first()

    def get_multi(self, db: Session):
        return db.query(User).all()

    def get_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def create_user(self, db: Session, user: SchemaUserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(username= user.username, email=user.email, password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    
user = CRUDUser()
