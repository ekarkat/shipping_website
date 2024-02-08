#!/usr/bin/python3
"""Parcel Model"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Parcel(BaseModel, Base):
    # Parcel class attribute
    __tablename__ = "parcels"
    from_name = Column(String(128), nullable=False)
    from_phone_number = Column(String(60), nullable=False)
    from_city = Column(String(60), nullable=False)
    to_name = Column(String(60), nullable=True)
    to_phone_number = Column(String(60), nullable=True)
    to_address = Column(String(1024), nullable=True)
    to_city = Column(String(60), nullable=True)
    to_postalcode = Column(String(60), nullable=True)
    parcel_weight = Column(String(60), nullable=True)
    parcel_tracking_number = Column(String(60), nullable=True)
    parcel_status = Column(String(60), nullable=True)
    parcel_pay_type = Column(String(60), nullable=True)
    parcel_user_id = Column(String(128), ForeignKey("users.id"), nullable=False)
    parcel_day_in_transist = Column(Integer, nullable=True)
    parcel_comments = Column(String(512), nullable=True)
