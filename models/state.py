#!/usr/bin/python3
"""User Model"""

from models.base_model import BaseModel, Base
from models.parcel import Parcel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class State(BaseModel, Base):
    # User attribute
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state_cities", cascade="all, delete")
