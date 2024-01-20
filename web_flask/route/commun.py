#!/usr/bin/python3
"""Registarion form rout"""
from flask import render_template, url_for, request

from web_flask import app


@app.route("/")
def home():
    return render_template("home.html")
