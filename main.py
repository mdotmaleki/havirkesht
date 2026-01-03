from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Farmer, Base
from schemas import FarmerCreate, Farmer
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/farmers/", response_model=Farmer)
def create_farmer(farmer: FarmerCreate, db: Session = Depends(get_db)):
    return crud.create_farmer(db=db, farmer=farmer)

@app.get("/farmers/{farmer_id}", response_model=Farmer)
def read_farmer(farmer_id: int, db: Session = Depends(get_db)):
    db_farmer = crud.get_farmer(db, farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@app.get("/farmers/", response_model=list[Farmer])
def read_farmers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_farmers(db, skip=skip, limit=limit)

@app.put("/farmers/{farmer_id}", response_model=Farmer)
def update_farmer(farmer_id: int, farmer: FarmerCreate, db: Session = Depends(get_db)):
    db_farmer = crud.update_farmer(db, farmer_id, farmer)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@app.delete("/farmers/{farmer_id}", response_model=Farmer)
def delete_farmer(farmer_id: int, db: Session = Depends(get_db)):
    db_farmer = crud.delete_farmer(db, farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

