from sqlalchemy import Column, BigInteger, String, DateTime, Integer, ForeignKey, ARRAY, Boolean
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 


class Farmer(Base):
    __tablename__ = "farmer"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    national_id = Column(String, nullable=True)
    full_name = Column(String, nullable=False)
    father_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    sheba_number_1 = Column(String, nullable=True)
    sheba_number_2 = Column(String, nullable=True)
    card_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())



class CropYearModel(Base):
    __tablename__ = "crop_year"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    crop_year_name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

class ProvinceModel(Base):
    __tablename__ = "province"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    province = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

class CityModel(Base):
    __tablename__ = "city"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    city = Column(String, nullable=False)
    province_id = Column(BigInteger, ForeignKey("province.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    province = relationship("ProvinceModel", backref="cities")

class VillageModel(Base):
    __tablename__ = "village"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    village = Column(String, nullable=False)
    city_id = Column(BigInteger, ForeignKey("city.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    city = relationship("CityModel", backref="villages")

class RoleModel(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    scopes = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    fullname = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    disabled = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    role = relationship("RoleModel", backref="users")

class FactoryModel(Base):
    __tablename__ = "factory"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    factory_name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  