#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, request, redirect
from web_flask import app
from flask_login import login_user, login_required, current_user
from web_flask.forms import CreateParcel, UserProfile


@app.route("/account/", methods=["GET", "POST"])
@login_required
def account():
    # Account route
    create_form = CreateParcel()
    user_profile = UserProfile()
    if create_form.validate_on_submit():
        parcel = {
            "to_name" : create_form.to_name.data,
            "to_phone_number" : create_form.to_phone_number.data,
            "to_address" : create_form.to_address.data,
            "to_city" : create_form.to_city.data,
            "parcel_weight" : create_form.parcel_weight.data,
            "parcel_comments" : create_form.parcel_comments.data,
        }
        print(parcel)
        current_user.create_parcel(**parcel)
        return redirect(url_for('account'))
    if user_profile.validate_on_submit():
        from models import storage
        user = storage.user_eamil(current_user.user_email)

    return render_template("account.html", create_form=create_form, user_profile=user_profile)
