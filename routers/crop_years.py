from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Farmer, Base
from schemas import FarmerCreate, Farmer
import crud
import schemas
from database import get_db
from routers import area, users, factory, crop_years
from routers.users import get_current_user

router = APIRouter(
    prefix="/crop_years",
    tags=["Crop Years"]
)




@router.post("/crop_years/", response_model=schemas.CropYear)
def create_crop_year(crop_year: schemas.CropYearCreate, db: Session = Depends(get_db),
                     current_user: schemas.User = Depends(get_current_user)):
    return crud.create_crop_year(db=db, crop_year=crop_year)

@router.get("/crop_years/{crop_year_id}", response_model=schemas.CropYear)
def read_crop_year(crop_year_id: int, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    db_crop_year = crud.get_crop_year(db, crop_year_id)
    if not db_crop_year:
        raise HTTPException(status_code=404, detail="Crop year not found")
    return db_crop_year

@router.get("/crop_years/", response_model=list[schemas.CropYear])
def read_crop_years(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                    current_user: schemas.User = Depends(get_current_user)):
    return crud.get_crop_years(db, skip=skip, limit=limit)

@router.put("/crop_years/{crop_year_id}", response_model=schemas.CropYear)
def update_crop_year(crop_year_id: int, crop_year: schemas.CropYearCreate, db: Session = Depends(get_db),
                     current_user: schemas.User = Depends(get_current_user)):
    db_crop_year = crud.update_crop_year(db, crop_year_id, crop_year)
    if not db_crop_year:
        raise HTTPException(status_code=404, detail="Crop year not found")
    return db_crop_year

@router.delete("/crop_years/{crop_year_id}", response_model=schemas.CropYear)
def delete_crop_year(crop_year_id: int, db: Session = Depends(get_db),
                     current_user: schemas.User = Depends(get_current_user)):
    db_crop_year = crud.delete_crop_year(db, crop_year_id)
    if not db_crop_year:
        raise HTTPException(status_code=404, detail="Crop year not found")
    return db_crop_year