import uvicorn
from fastapi import FastAPI, Request
from app.db.init_db import init_db
from app.api.api_v1.api import api_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Alexa API", debug=True)

init_db()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

app.include_router(api_router, prefix="/api_v1")
