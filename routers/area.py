from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from routers.users import get_current_user
import crud, schemas

router = APIRouter(
    prefix="/areas",
    tags=["Areas"]
)

@router.post("/provinces/", response_model=schemas.Province)
def create_province(province: schemas.ProvinceCreate, db: Session = Depends(get_db),
                    current_user: schemas.User = Depends(get_current_user)):
    return crud.create_province(db=db, province=province)

@router.get("/provinces/{province_id}", response_model=schemas.Province)
def read_province(province_id: int, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    db_province = crud.get_province(db, province_id)
    if not db_province:
        raise HTTPException(status_code=404, detail="Province not found")
    return db_province

@router.get("/provinces/", response_model=list[schemas.Province])
def read_provinces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.get_provinces(db, skip=skip, limit=limit)

@router.put("/provinces/{province_id}", response_model=schemas.Province)
def update_province(province_id: int, province: schemas.ProvinceCreate, db: Session = Depends(get_db),
                    current_user: schemas.User = Depends(get_current_user)):
    db_province = crud.update_province(db, province_id, province)
    if not db_province:
        raise HTTPException(status_code=404, detail="Province not found")
    return db_province

@router.delete("/provinces/{province_id}", response_model=schemas.Province)
def delete_province(province_id: int, db: Session = Depends(get_db),
                    current_user: schemas.User = Depends(get_current_user)):
    db_province = crud.delete_province(db, province_id)
    if not db_province:
        raise HTTPException(status_code=404, detail="Province not found")
    return db_province


@router.post("/cities/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_city(db=db, city=city)

@router.get("/cities/{city_id}", response_model=schemas.City)
def read_city(city_id: int, db: Session = Depends(get_db),
              current_user: schemas.User = Depends(get_current_user)):
    db_city = crud.get_city(db, city_id)
    if not db_city:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@router.get("/cities/", response_model=list[schemas.City])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.get_cities(db, skip=skip, limit=limit)

@router.put("/cities/{city_id}", response_model=schemas.City)
def update_city(city_id: int, city: schemas.CityCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_city = crud.update_city(db, city_id, city)
    if not db_city:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@router.delete("/cities/{city_id}", response_model=schemas.City)
def delete_city(city_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db_city = crud.delete_city(db, city_id)
    if not db_city:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@router.post("/villages/", response_model=schemas.Village)
def create_village(village: schemas.VillageCreate, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.create_village(db=db, village=village)

@router.get("/villages/", response_model=list[schemas.Village])
def read_villages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    return crud.get_villages(db, skip=skip, limit=limit)

@router.get("/villages/{village_id}", response_model=schemas.Village)
def read_village(village_id: int, db: Session = Depends(get_db),
                 current_user: schemas.User = Depends(get_current_user)):
    db_village = crud.get_village(db, village_id)
    if not db_village:
        raise HTTPException(status_code=404, detail="Village not found")
    return db_village

@router.put("/villages/{village_id}", response_model=schemas.Village)
def update_village(village_id: int, village: schemas.VillageCreate, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    db_village = crud.update_village(db, village_id, village)
    if not db_village:
        raise HTTPException(status_code=404, detail="Village not found")
    return db_village

@router.delete("/villages/{village_id}", response_model=schemas.Village)
def delete_village(village_id: int, db: Session = Depends(get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    db_village = crud.delete_village(db, village_id)
    if not db_village:
        raise HTTPException(status_code=404, detail="Village not found")
    return db_village

@router.get("/villages/{village_id}/info", response_model=schemas.VillageInfo)
def get_village_info(village_id: int, db: Session = Depends(get_db),
                     current_user: schemas.User = Depends(get_current_user)):
    db_village = crud.get_village_with_relations(db, village_id)
    if not db_village:
        raise HTTPException(status_code=404, detail="Village not found")

    return {
        "village": db_village.village,
        "city": db_village.city.city,
        "province": db_village.city.province.province
    }
