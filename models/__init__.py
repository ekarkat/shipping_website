#!/usr/bin/python3
"""This module instantiates an object of class dbstorage"""
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
