#!/usr/bin/python3
"""Registarion form rout"""

from flask import render_template, url_for, request
from web_flask import app
from models.user import User
from models import storage


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("*********************** post request ******************** \n")
        imput = {
            "user_full_name" : request.form.get("full_name"),
            "user_email" : request.form.get("email"),
            "user_password" : request.form.get("password"),
            "user_phone_number" : request.form.get("phone"),
            "user_city" : request.form.get("city"),
            "user_address" : request.form.get("address"),
            "user_birth_date" : request.form.get("birth_date")
        }
        new_user = User(**imput)
        new_user.save()
        return render_template("home.html")
    if request.method == 'GET':
        print("\n \n \n******************* get method *************************")

    return render_template("register.html")