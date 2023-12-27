#!/usr/bin/python3
"""Parcel Model"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Parcel(BaseModel, Base):
    # Parcel class attribute
    __tablename__ = "parcels"
    sender_name = Column(String(128), nullable=False)
    sender_phone_number = Column(String(60), nullable=False)
    sender_city = Column(String(60), nullable=False)
    receiver_name = Column(String(60), nullable=True)
    receiver_phone_number = Column(String(60), nullable=True)
    receiver_address = Column(String(1024), nullable=True)
    receiver_city = Column(String(60), nullable=True)
    parcel_weight = Column(String(60), nullable=True)
    parcel_tracking_number = Column(String(60), nullable=True)
    parcel_status = Column(String(60), nullable=True)
    parcel_pay_type = Column(String(60), nullable=True)
    parcel_user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
