from sqlalchemy.orm import Session
from models import Farmer
from schemas import FarmerCreate


def create_farmer(db: Session, farmer: FarmerCreate):
    db_farmer = Farmer(**farmer.dict())
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def get_farmer(db: Session, farmer_id: int):
    return db.query(Farmer).filter(Farmer.id == farmer_id).first()

def get_all_farmers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Farmer).offset(skip).limit(limit).all()

def update_farmer(db: Session, farmer_id: int, farmer: FarmerCreate):
    db_farmer = db.query(Farmer).filter(Farmer.id == farmer_id).first()
    if not db_farmer:
        return None
    for key, value in farmer.dict().items():
        setattr(db_farmer, key, value)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def delete_farmer(db: Session, farmer_id: int):
    db_farmer = db.query(Farmer).filter(Farmer.id == farmer_id).first()
    if not db_farmer:
        return None
    db.delete(db_farmer)
    db.commit()
    return db_farmer

