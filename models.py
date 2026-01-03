from sqlalchemy import Column, BigInteger, String, DateTime
from database import Base
from datetime import datetime
from sqlalchemy.sql import func


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
    #created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    #updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    #created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    #updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())





