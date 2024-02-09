#!/usr/bin/python3
"""
    Flask route that returns json response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State

method = ['PUT', 'GET', 'POST', 'DELETE']
@app_views.route('/states/', strict_slashes=False,
                 methods=method)
def all_states():
	states = []
	for key, value in storage.all("State").items():
		states.append(value.to_dict())
	return jsonify(states)

@app_views.route('/states/cities/<id>', strict_slashes=False,
                 methods=method)
def all_state_cities(id):
	cities = []
	state = storage.ses().query(State).filter_by(id=id).all()
	if not state:
		abort(404)
	state = state[0]
	for city in state.cities:
		cities.append(city.to_dict())
	return jsonify(cities)
