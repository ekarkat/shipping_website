#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, request, redirect, jsonify
from web_flask import app
from flask_login import login_user, login_required, current_user
from web_flask.forms import CreateParcel, UserProfile, ContactUs
import models
import requests



@app.route("/dist/<info>/")
def dist(info):
    splitted_strings = info.split("-")
    origin = splitted_strings[0]
    destination = splitted_strings[1]
    api_key = "AIzaSyBea9ip3bUMm-Z6jcl1Yk9m4lqHiwCpDjs"
    mo = ', Morocco'
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin+mo}&destinations={destination+mo}&key={api_key}"

    response = requests.get(url)
    data = response.json()
    statu_code = data.get("rows")[0].get("elements")[0].get("status")
    if statu_code == "NOT_FOUND":
        distance_text = 0
    distance_text = data.get("rows")[0].get("elements")[0].get("distance").get("text")
    distance_num = float(distance_text[:-3])

    # return jsonify(data), 201
    return jsonify({'distance':distance_num}), 201
