from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Farmer, Base
from schemas import FarmerCreate, Farmer
import crud
import schemas
from routers import area, users, factory, farmers, crop_years
from routers.users import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





app.include_router(area.router)

app.include_router(users.router)

app.include_router(factory.router)

app.include_router(farmers.router)

app.include_router(crop_years.router)