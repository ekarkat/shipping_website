#!/usr/bin/python3
"""Registarion form rout"""
from flask import render_template, url_for, request

from web_flask import app
from flask_cors import CORS


CORS(app, origins="0.0.0.0")

@app.route("/test/")
def test():
    return render_template("test.html")
