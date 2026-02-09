from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Farmer, Base
from schemas import FarmerCreate, Farmer
import crud
import schemas
from database import get_db
from routers import area, users, factory
from routers.users import get_current_user

router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)


@router.post("/farmers/", response_model=Farmer)
def create_farmer(farmer: FarmerCreate, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    return crud.create_farmer(db=db, farmer=farmer)

@router.get("/farmers/{farmer_id}", response_model=Farmer)
def read_farmer(farmer_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_farmer = crud.get_farmer(db, farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@router.get("/farmers/", response_model=list[Farmer])
def read_farmers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                 current_user: schemas.User = Depends(get_current_user)):
    return crud.get_all_farmers(db, skip=skip, limit=limit)

@router.put("/farmers/{farmer_id}", response_model=Farmer)
def update_farmer(farmer_id: int, farmer: FarmerCreate, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    db_farmer = crud.update_farmer(db, farmer_id, farmer)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@router.delete("/farmers/{farmer_id}", response_model=Farmer)
def delete_farmer(farmer_id: int, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    db_farmer = crud.delete_farmer(db, farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer