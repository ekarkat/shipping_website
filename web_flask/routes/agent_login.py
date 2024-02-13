#!/usr/bin/python3
"""Login form route"""

from flask import render_template, url_for, request, redirect
from web_flask import app, bycpt, login_manager
from web_flask.forms import AgentLogin
from flask_login import login_user, logout_user, current_user


@app.route("/agent-login/", methods=["GET", "POST"])
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

        return render_template("agent_login.html", form=form)

    return render_template("agent_login.html", form=form)

# @app.route("/logout-agent")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))
