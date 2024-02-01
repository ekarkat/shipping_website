#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, request, redirect
from web_flask import app
from flask_login import login_user, login_required, current_user
from web_flask.forms import CreateParcel, UserProfile
import models
from flask_cors import CORS


CORS(app, origins="0.0.0.0")

@app.route("/account/", methods=["GET", "POST"])
@login_required
def account():
    # Account route
    create_form = CreateParcel()
    profile_form = UserProfile()

    if profile_form.validate_on_submit():
		# if user submit in edit profile
        print(profile_form.email.data)
        return redirect(url_for('account'))

    if create_form.validate_on_submit():
		# if user create a parcel
        parcel = {
            "to_name" : create_form.to_name.data,
            "to_phone_number" : create_form.to_phone_number.data,
            "to_address" : create_form.to_address.data,
            "to_city" : create_form.to_city.data,
            "to_postalcode" : create_form.to_postalcode.data,
            "parcel_weight" : create_form.parcel_weight.data,
            "parcel_comments" : create_form.parcel_comments.data,
        }
        # print(parcel)
        current_user.create_parcel(**parcel)
        return redirect(url_for('account'))

    parcels = current_user.user_parcels
    # print(parcels)

    return render_template("account.html", profile_form=profile_form, create_form=create_form, parcels=parcels)
