#!/usr/bin/python3
"""Agent Model"""

from models.base_model import BaseModel, Base
from models.parcel import Parcel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from flask_login import UserMixin


class Agent(BaseModel, Base, UserMixin):
    # User attribute
    __tablename__ = "agents"
    agent_full_name = Column(String(128), nullable=False)
    agent_email = Column(String(128), nullable=False)
    agent_password = Column(String(128), nullable=False)
    agent_phone_number = Column(String(32), nullable=False)
    agent_state = Column(String(60), nullable=False)
    agent_city = Column(String(60), nullable=False)
    agent_address = Column(String(1024), nullable=False)
    agent_postalcode = Column(String(12), nullable=True)
    agent_birth_date = Column(String(10), nullable=True)
    agent_parcels = relationship("Parcel", backref="agent_parcels")

    def pickup(self, tr):
        # Method for agent to pick up
        from models import storage
        from models.parcel import Parcel
        parcel = storage.parcel_track(tr)
        if not parcel:
            return None
        agent_details = {
            "parcel_agent_id" : self.id,
            "parcel_status" : "On delivery to " + parcel.to_city,
            "parcel_history" : parcel.parcel_status + ":" + "Picked up by shipping company:" + "On delivery to " + parcel.to_city + ":",
            }
        parcel.update(**agent_details)
        parcel.save()
        return(parcel)

    def deliver(self, tr):
        # Method for agent to deliver
        from models import storage
        from models.parcel import Parcel
        parcel = storage.parcel_track(tr)
        if not parcel:
            return None
        agent_details = {
            "parcel_agent_id" : self.id,
            "parcel_status" : "Recieved by " + parcel.to_name,
            "parcel_history" : parcel.parcel_history + ":" + "Recieved by " + parcel.to_name,
            }
        parcel.update(**agent_details)
        parcel.save()
        return(parcel)
