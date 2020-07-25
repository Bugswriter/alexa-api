from pydantic import BaseModel

class SpotCreate(BaseModel):
    name : str
    location : str
    info : str
    special_attraction : str
    thigns_to_do : str
    time_to_visit : str
    near_by_places : str
    similar_places : str
    how_to_reach : str
