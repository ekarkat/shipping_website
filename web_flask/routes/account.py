#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, request
from web_flask import app
from flask_login import login_user, login_required, current_user


@app.route("/account")
@login_required
def account():
    # Account route
    return render_template("account.html")
