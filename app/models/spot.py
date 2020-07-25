from sqlalchemy import Column, String, Integer, Boolean
from app.db.database import Base


class Spot(Base):
    __tablename__ = "spot"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    info = Column(String)
    special_attraction = Column(String)
    thigns_to_do = Column(String)
    time_to_visit = Column(String)
    near_by_places = Column(String)
    similar_places = Column(String)
    how_to_reach = Column(String)
