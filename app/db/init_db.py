from app.models import user, spot
from app.db.database import engine

def init_db():
    user.Base.metadata.create_all(bind=engine)
    spot.Base.metadata.create_all(bind=engine)
