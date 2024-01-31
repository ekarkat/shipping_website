#!/usr/bin/bash
"""Database storage class"""

from models.base_model import BaseModel, Base
from models.user import User
from models.parcel import Parcel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sys import argv

class DBStorage():
    # Database storage class
    __engine = None
    __session = None

    def __init__(self):
        """Start engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                        format(("root"),
                                                ("root"),
                                                ("localhost"),
                                                ("ship_db")),
                                        pool_pre_ping=True)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs_dic = {}
        if not cls:
            result = self.__session.query(User).all()
            result.extend(self.__session.query(Parcel).all())
        else:
            if isinstance(cls, str):
                result = self.__session.query(eval(cls)).all()
            else:
                result = self.__session.query(cls).all()
        for obj in result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objs_dic[key] = obj
        return (objs_dic)

    def user_eamil(self, email):
        """Returns a user based on email"""
        result = self.__session.query(User).filter_by(user_email=email).all()
        if len(result) == 0:
            return None
        return (result[0])

    def user_id(self, id):
        """Returns a user based on id"""
        result = self.__session.query(User).filter_by(id=id).all()
        if len(result) == 0:
            return None
        return (result[0])

    def parcel_id(self, id):
        """Returns a user based on id"""
        result = self.__session.query(Parcel).filter_by(id=id).all()
        if len(result) == 0:
            return None
        return (result[0])

    def new(self, obj):
        """Add obj to database"""
        self.__session.add(obj)

    def save(self):
        """commit changes in database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        # close a session
        self.__session.close()
