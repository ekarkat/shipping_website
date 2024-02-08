#!/usr/bin/python3
"""Login form route"""

from flask import render_template, url_for, request, redirect
from web_flask import app, bycpt, login_manager
from web_flask.forms import LoginForm
from flask_login import login_user, logout_user, current_user


@app.route("/login/", methods=["GET", "POST"])
def login():
    # Login route
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        from models import storage
        user = storage.user_by_email(form.email.data)
        if user and bycpt.check_password_hash(user.user_password, form.password.data):
            login_user(user)
            return render_template("home.html")

        return render_template("login.html", form=form)

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))