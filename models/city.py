#!/usr/bin/python3
"""User Model"""

from models.base_model import BaseModel, Base
from models.parcel import Parcel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class City(BaseModel, Base):
    # User attribute
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey("states.id"), nullable=False)