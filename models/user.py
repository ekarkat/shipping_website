#!/usr/bin/python3
"""User Model"""

from models.base_model import BaseModel, Base
from models.parcel import Parcel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from web_flask import app
import random
import string


def generate_unique_code():
    from models import storage
    # Generate a 10-digit random code
    code = 'MA'+''.join(str(random.randint(0, 9)) for _ in range(9)) + random.choice(string.ascii_uppercase)
    # Check if the generated code is already in use
    while storage.parcel_track(code):
        # If it's in use, generate a new code
        code = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return code

class User(BaseModel, Base, UserMixin):
    # User attribute
    __tablename__ = "users"
    user_full_name = Column(String(128), nullable=False)
    user_email = Column(String(128), nullable=False)
    user_password = Column(String(128), nullable=False)
    user_phone_number = Column(String(32), nullable=False)
    user_city = Column(String(60), nullable=False)
    user_address = Column(String(1024), nullable=False)
    user_birth_date = Column(String(10), nullable=True)
    user_parcels = relationship("Parcel", backref="user_parcels", cascade="all, delete")

    def create_parcel(self, **kwargs):
        # Method for user to create a parcel
        track_num = generate_unique_code()
        user_details = {
            "from_name" : self.user_full_name,
            "from_phone_number" : self.user_phone_number,
            "from_city" : self.user_city,
            "parcel_user_id" : self.id,
            "parcel_tracking_number": track_num,
            "parcel_status": "Ready for Pickup"
            }
        details ={**user_details, **kwargs}
        parcel = Parcel(**details)
        parcel.save()
        return(parcel)
    

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        from models import storage
        return storage.user_id(user_id)
