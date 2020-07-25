from sqlalchemy import Column, String, Integer, Boolean
from app.db.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)