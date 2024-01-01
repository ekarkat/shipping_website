#!/usr/bin/python3
"""User Model"""

from models.base_model import BaseModel, Base
from models.parcel import Parcel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class User(BaseModel, Base):
    # User attribute
    __tablename__ = "users"
    user_full_name = Column(String(128), nullable=False)
    user_email = Column(String(128), nullable=False)
    user_password = Column(String(128), nullable=False)
    user_phone_number = Column(String(32), nullable=False)
    user_city = Column(String(60), nullable=False)
    user_address = Column(String(1024), nullable=False)
    user_birth_date = Column(String(16), nullable=True)
    user_parcels = relationship("Parcel",  backref="user_parcels", cascade="all, delete")

    def create_parcel(self, **kwargs):
        # Method for user to create a parcel
        user_details = {
            "sender_name" : self.user_full_name,
            "sender_phone_number" : self.user_phone_number,
            "sender_city" : self.user_city,
            "parcel_user_id" : self.id
            }
        details ={**user_details, **kwargs}
        parcel = Parcel(**details)
        return(parcel)
