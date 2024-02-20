#!/usr/bin/python3
"""Login form route"""

from flask import render_template, url_for, request, redirect
from web_flask import app, bycpt, login_manager
from web_flask.forms import AgentLogin, RegisterForm
from flask_login import login_user, logout_user, current_user
import models

@app.route("/agent-register/", methods=["GET", "POST"], subdomain="agent")
def agent_register():
    # register route
    if current_user.is_authenticated:
        return redirect(url_for('agent_account'))

    form = RegisterForm()
    if form.validate_on_submit():
        from models.agent import Agent
        from models.state import State
        from models.city import City
        hashed_pass = bycpt.generate_password_hash(form.password.data).decode("utf-8")
        state = models.storage.ses().query(State).filter_by(id=request.form['states']).first()
        city = models.storage.ses().query(City).filter_by(id=request.form['cities']).first()
        imput = {
            "agent_full_name" : form.full_name.data,
            "agent_email" : form.email.data,
            "agent_password" : hashed_pass,
            "agent_phone_number" : form.phone.data,
            "agent_state" : state.name,
            "agent_city" : city.name,
            "agent_address" : form.address.data,
            "agent_postalcode" : form.postal_code.data,
            "agent_birth_date" : form.birth_date.data,
        }

        new_user = Agent(**imput)
        new_user.save()
        return redirect(url_for('agent_login'))

    states = []
    for key, value in models.storage.all("State").items():
        states.append(value)
    
    return render_template("register.html", form=form, states=states, title='Register')


@app.route("/agent-login/", methods=["GET", "POST"], subdomain="agent")
def agent_login():
    # Login route
    if current_user.is_authenticated:
        return redirect(url_for('agent_account'))

    form = AgentLogin()
    if form.validate_on_submit():
        from models import storage
        agent = storage.agent_eamil(form.email.data)
        print(agent)
        if agent:
            login_user(agent)
            return redirect(url_for('agent_account'))

        return render_template("agent_login.html", form=form, title='Login')

    return render_template("agent_login.html", form=form, title='Login')

# @app.route("/logout-agent")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))
