from pydantic import BaseModel, ConfigDict
from datetime import datetime
from sqlalchemy import TIMESTAMP

#--------------------------Farmer-------------------------------------
class FarmerBase(BaseModel):
    national_id: str | None = None
    full_name: str
    father_name: str | None = None
    phone_number: str | None = None
    sheba_number_1: str | None = None
    sheba_number_2: str | None = None
    card_number: str | None = None
    address: str | None = None

class FarmerCreate(FarmerBase):
    pass

class Farmer(FarmerBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None


    class Config:
        from_attributes = True
#------------------------End Of Farmer-----------------------------------

class CropYearBase(BaseModel):
    crop_year_name: str

class CropYearCreate(CropYearBase):
    pass

class CropYear(CropYearBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class ProvinceBase(BaseModel):
    province: str

class ProvinceCreate(ProvinceBase):
    pass

class Province(ProvinceBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class CityBase(BaseModel):
    city: str
    province_id: int

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class VillageBase(BaseModel):
    village: str
    city_id: int

class VillageCreate(VillageBase):
    pass

class Village(VillageBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class VillageInfo(BaseModel):
    village: str
    city: str
    province: str

class RoleBase(BaseModel):
    name: str
    scopes: list[str] | None = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)





class UserBase(BaseModel):
    username: str
    fullname: str | None = None
    phone_number: str | None = None
    email: str | None = None
    disabled: bool = False
    role_id: int | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class FactoryBase(BaseModel):
    factory_name: str

class FactoryCreate(FactoryBase):
    pass

class Factory(FactoryBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)