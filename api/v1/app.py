#!/usr/bin/python3
'''Flask web application API
'''
from os import getenv
from flask import Flask, make_response, jsonify
import models
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__, subdomain_matching=False)
CORS(app, origins='*')
app.config['SERVER_NAME'] = "shippit.us"
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    models.storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """closes the storage on teardown"""
    return {"error": "Not found"}, 404


host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5600)
if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
