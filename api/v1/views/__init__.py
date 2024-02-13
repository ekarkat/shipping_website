#!/usr/bin/pyhon3
'''the blueprint for the API.'''
from flask import Flask, Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.users import *
from api.v1.views.parcels import *
from api.v1.views.states import *
