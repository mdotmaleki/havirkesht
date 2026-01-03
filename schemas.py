from pydantic import BaseModel
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

