#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel():
    # Base Model Class

    # Time format for time
    t_f = "%Y-%m-%d %H:%M:%S"
    __dato = lambda t_f:datetime.strptime(datetime.utcnow().strftime(t_f), t_f)


    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, **kwargs):
        # init methode for base model
        if not kwargs:
            print ("no kwargs")
            self.id = str(uuid.uuid4())
            self.created_at = BaseModel.__dato(BaseModel.t_f)
            self.updated_at = BaseModel.__dato(BaseModel.t_f)
        else:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = BaseModel.__dato(BaseModel.t_f)
            else:
                self.created_at = datetime.strptime(kwargs["created_at"], BaseModel.t_f)
            if "updated_at" not in kwargs:
                self.updated_at = BaseModel.__dato(BaseModel.t_f)
            else:
                self.updated_at = datetime.strptime(kwargs["updated_at"], BaseModel.t_f)
            for key, value in kwargs.items():
                if key not in ["__class__", "updated_at", "created_at"]:
                    setattr(self, key, value)

    def __str__(self):
        # format [class name]:<id> : {dict}
        class_name = type(self).__name__
        output = "[{}] : {} : {} ".format(class_name, self.id, self.__dict__)
        return (output)

    def to_dict(self):
        # Return a dictionary representation of object
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key not in ["__class__", "updated_at", "created_at"]:
                obj_dict[key] = value
            if key == '__class__':
                class_name = type(self).__name__
                obj_dict[key] = class_name
            if key == "updated_at":
                updated_at = value.strftime(BaseModel.t_f)
                obj_dict[key] = updated_at
            if key == "created_at":
                created_at = value.strftime(BaseModel.t_f)
                obj_dict[key] = created_at
        del obj_dict['_sa_instance_state']
        return (obj_dict)

    def update(self, **kwargs):
        # update an object
        for key, value in kwargs.items():
            if key not in ["__class__", "updated_at", "created_at"]:
                setattr(self, key, value)
            if key == '__class__':
                continue
            if key == "updated_at":
                updated_at = datetime.strptime(value, BaseModel.t_f)
                setattr(self, key, value)
            if key == "created_at":
                created_at = datetime.strptime(value, BaseModel.t_f)
                setattr(self, key, value)

    def save(self):
        """save a model"""
        from models import storage
        self.updated_at = BaseModel.__dato(BaseModel.t_f)
        storage.new(self)
        storage.save()

    def delete(self):
        from models import storage
        storage.delete(self)



