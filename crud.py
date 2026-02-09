from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Farmer, CropYearModel, ProvinceModel , CityModel, VillageModel, RoleModel, UserModel, FactoryModel
import models
from schemas import FarmerCreate, CropYearCreate, ProvinceCreate, CityCreate, VillageCreate, RoleCreate, UserCreate, FactoryCreate
from passlib.context import CryptContext

import schemas

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

def create_crop_year(db: Session, crop_year: CropYearCreate):
    db_crop_year = CropYearModel(**crop_year.model_dump())
    db.add(db_crop_year)
    db.commit()
    db.refresh(db_crop_year)
    return db_crop_year

def get_crop_year(db: Session, crop_year_id: int):
    return db.query(CropYearModel).filter(CropYearModel.id == crop_year_id).first()

def get_crop_years(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CropYearModel).offset(skip).limit(limit).all()

def update_crop_year(db: Session, crop_year_id: int, crop_year: CropYearCreate):
    db_crop_year = db.query(CropYearModel).filter(CropYearModel.id == crop_year_id).first()
    if not db_crop_year:
        return None
    for key, value in crop_year.model_dump().items():
        setattr(db_crop_year, key, value)
    db.commit()
    db.refresh(db_crop_year)
    return db_crop_year

def delete_crop_year(db: Session, crop_year_id: int):
    db_crop_year = db.query(CropYearModel).filter(CropYearModel.id == crop_year_id).first()
    if not db_crop_year:
        return None
    db.delete(db_crop_year)
    db.commit()
    return db_crop_year

def create_province(db: Session, province: ProvinceCreate):
    db_province = ProvinceModel(**province.model_dump())
    db.add(db_province)
    db.commit()
    db.refresh(db_province)
    return db_province

def get_province(db: Session, province_id: int):
    return db.query(ProvinceModel).filter(ProvinceModel.id == province_id).first()

def get_provinces(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProvinceModel).offset(skip).limit(limit).all()

def update_province(db: Session, province_id: int, province: ProvinceCreate):
    db_province = db.query(ProvinceModel).filter(ProvinceModel.id == province_id).first()
    if not db_province:
        return None
    for key, value in province.model_dump().items():
        setattr(db_province, key, value)
    db.commit()
    db.refresh(db_province)
    return db_province

def delete_province(db: Session, province_id: int):
    db_province = db.query(ProvinceModel).filter(ProvinceModel.id == province_id).first()
    if not db_province:
        return None
    db.delete(db_province)
    db.commit()
    return db_province

def create_city(db: Session, city: CityCreate):
    db_city = CityModel(**city.model_dump())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CityModel).offset(skip).limit(limit).all()

def get_city(db: Session, city_id: int):
    return db.query(CityModel).filter(CityModel.id == city_id).first()

def update_city(db: Session, city_id: int, city: CityCreate):
    db_city = db.query(CityModel).filter(CityModel.id == city_id).first()
    if not db_city:
        return None
    for key, value in city.model_dump().items():
        setattr(db_city, key, value)
    db.commit()
    db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = db.query(CityModel).filter(CityModel.id == city_id).first()
    if not db_city:
        return None
    db.delete(db_city)
    db.commit()
    return db_city

def create_village(db: Session, village: VillageCreate):
    db_village = VillageModel(**village.model_dump())
    db.add(db_village)
    db.commit()
    db.refresh(db_village)
    return db_village

def get_villages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(VillageModel).offset(skip).limit(limit).all()

def get_village(db: Session, village_id: int):
    return db.query(VillageModel).filter(VillageModel.id == village_id).first()

def update_village(db: Session, village_id: int, village: VillageCreate):
    db_village = db.query(VillageModel).filter(VillageModel.id == village_id).first()
    if not db_village:
        return None
    for key, value in village.model_dump().items():
        setattr(db_village, key, value)
    db.commit()
    db.refresh(db_village)
    return db_village

def delete_village(db: Session, village_id: int):
    db_village = db.query(VillageModel).filter(VillageModel.id == village_id).first()
    if not db_village:
        return None
    db.delete(db_village)
    db.commit()
    return db_village

def get_village_with_relations(db: Session, village_id: int):
    return db.query(VillageModel).filter(VillageModel.id == village_id).first()

def create_role(db: Session, role: RoleCreate):
    db_role = RoleModel(**role.model_dump())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RoleModel).offset(skip).limit(limit).all()

def get_role(db: Session, role_id: int):
    return db.query(RoleModel).filter(RoleModel.id == role_id).first()

def update_role(db: Session, role_id: int, role: RoleCreate):
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if not db_role:
        return None
    for key, value in role.model_dump().items():
        setattr(db_role, key, value)
    db.commit()
    db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if not db_role:
        return None
    db.delete(db_role)
    db.commit()
    return db_role

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)




def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)

    db_user = models.UserModel(
        username=user.username,
        fullname=user.fullname,
        phone_number=user.phone_number,
        email=user.email,
        password=hashed_password,
        role_id=user.role_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user




def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return None
    for key, value in user.model_dump(exclude={"password"}).items():
        setattr(db_user, key, value)
    if user.password:
        db_user.password = get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def create_factory(db: Session, factory: FactoryCreate):
    db_factory = FactoryModel(**factory.model_dump())
    db.add(db_factory)
    db.commit()
    db.refresh(db_factory)
    return db_factory  

def get_factory(db: Session, factory_id: int):
    return db.query(FactoryModel).filter(FactoryModel.id == factory_id).first()

def get_factories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FactoryModel).offset(skip).limit(limit).all()

def update_factory(db: Session, factory_id: int, factory: FactoryCreate):
    db_factory = db.query(FactoryModel).filter(FactoryModel.id == factory_id).first()
    if not db_factory:
        return None
    for key, value in factory.model_dump().items():
        setattr(db_factory, key, value)
    db.commit()
    db.refresh(db_factory)
    return db_factory

def delete_factory(db: Session, factory_id: int):
    db_factory = db.query(FactoryModel).filter(FactoryModel.id == factory_id).first()
    if not db_factory:
        return None
    db.delete(db_factory)
    db.commit()
    return db_factory