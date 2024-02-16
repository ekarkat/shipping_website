#!/usr/bin/python3
"""Registarion form route"""

from flask import render_template, url_for, request, redirect
from web_flask import app, bycpt
from web_flask.forms import RegisterForm, LoginForm
from flask_login import current_user
import models

@app.route("/register/", methods=["GET", "POST"])
def register():
    # register route
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        from models.user import User
        from models.state import State
        from models.city import City
        hashed_pass = bycpt.generate_password_hash(form.password.data).decode("utf-8")
        state = models.storage.ses().query(State).filter_by(id=request.form['states']).first()
        city = models.storage.ses().query(City).filter_by(id=request.form['cities']).first()
        imput = {
            "user_full_name" : form.full_name.data,
            "user_email" : form.email.data,
            "user_password" : hashed_pass,
            "user_phone_number" : form.phone.data,
            "user_state" : state.name,
            "user_city" : city.name,
            "user_address" : form.address.data,
            "user_postalcode" : form.postal_code.data,
            "user_birth_date" : form.birth_date.data,
        }

        new_user = User(**imput)
        new_user.save()
        return redirect(url_for('login'))

    states = []
    for key, value in models.storage.all("State").items():
        states.append(value)
    
    return render_template("register.html", form=form, states=states, title='Register')
