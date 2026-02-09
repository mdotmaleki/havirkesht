from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.users import get_current_user
import crud, schemas

router = APIRouter(
    prefix="/factory",
    tags=["Factory"]
    )

@router.post("/", response_model=schemas.Factory)
def create_factory(factory: schemas.FactoryCreate, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.create_factory(db=db, factory=factory)

@router.get("/{factory_id}", response_model=schemas.Factory)
def read_factory(factory_id: int, db: Session = Depends(get_db),
                 current_user: schemas.User = Depends(get_current_user)):
    db_factory = crud.get_factory(db, factory_id)
    if not db_factory:
        raise HTTPException(status_code=404, detail="Factory not found")
    return db_factory

@router.get("/", response_model=list[schemas.Factory])
def read_factories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.get_factories(db, skip=skip, limit=limit)

@router.put("/{factory_id}", response_model=schemas.Factory)
def update_factory(factory_id: int, factory: schemas.FactoryCreate, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    db_factory = crud.update_factory(db, factory_id, factory)
    if not db_factory:
        raise HTTPException(status_code=404, detail="Factory not found")
    return db_factory

@router.delete("/{factory_id}", response_model=schemas.Factory)
def delete_factory(factory_id: int, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    db_factory = crud.delete_factory(db, factory_id)
    if not db_factory:
        raise HTTPException(status_code=404, detail="Factory not found")
    return db_factory