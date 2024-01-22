#!/usr/bin/python3
"""Registarion form rout"""

from flask import render_template, url_for, request
from web_flask import app, bycpt
from web_flask.forms import RegisterForm, LoginForm


@app.route("/register/", methods=["GET", "POST"])
def register():
    # register route
    form = RegisterForm()
    if form.validate_on_submit():
        from models.user import User
        hashed_pass = bycpt.generate_password_hash(form.password.data).decode("utf-8")
        imput = {
            "user_full_name" : form.full_name.data,
            "user_email" : form.email.data,
            "user_password" : hashed_pass,
            "user_phone_number" : form.phone.data,
            "user_city" : form.city.data,
            "user_address" : form.address.data,
            "user_birth_date" : form.birth_date.data
        }

        new_user = User(**imput)
        new_user.save()
        return render_template("home.html")
    return render_template("register.html", form=form)
