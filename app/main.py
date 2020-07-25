import uvicorn
from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.api_v1.api import api_router

app = FastAPI(title="Alexa API", debug=True)

init_db()

app.include_router(api_router, prefix="/api_v1")
