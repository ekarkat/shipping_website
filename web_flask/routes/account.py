#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, request, redirect
from web_flask import app
from flask_login import login_user, login_required, current_user
from web_flask.forms import CreateParcel, UserProfile, ContactUs
import models


@app.route("/account/", methods=["GET", "POST"])
@login_required
def account():
    # Account route
    create_form = CreateParcel()
    profile_form = UserProfile()
    contactus = ContactUs()

    if profile_form.validate_on_submit():
        # if user submit in edit profile
        user = current_user
        from models.state import State
        from models.city import City
        state = models.storage.ses().query(State).filter_by(id=request.form['states']).first().name
        city = models.storage.ses().query(City).filter_by(id=request.form['cities']).first().name
        user_dic = {
            "user_full_name" : profile_form.full_name.data,
            "user_email" : profile_form.email.data,
            "user_state" : state,
            "user_city" : city,
            "user_address" : profile_form.address.data,
            "user_postalcode" : profile_form.postal_code.data,
            "user_birth_date" : profile_form.birth_date.data,
        }
        user.update(**user_dic)
        user.save()

    if contactus.validate_on_submit():
        # if user submit in edit profile
        print(contactus.message.data)
        return redirect(url_for('account'))

    if create_form.validate_on_submit():
        # if user create a parcel
        from models.state import State
        from models.city import City
        state = models.storage.ses().query(State).filter_by(id=request.form['states']).first().name
        city = models.storage.ses().query(City).filter_by(id=request.form['cities']).first().name

        parcel = {
            "to_name" : create_form.to_name.data,
            "to_phone_number" : create_form.to_phone_number.data,
            "to_address" : create_form.to_address.data,
            "to_state" : state,
            "to_city" : city,
            "to_postalcode" : create_form.to_postalcode.data,
            "parcel_type" : request.form['parcel_type'],
            "parcel_cost" : create_form.parcel_cost.data,
            "parcel_weight" : create_form.parcel_weight.data,
            "parcel_comments" : create_form.parcel_comments.data,
        }
        # print(parcel)
        current_user.create_parcel(**parcel)
        return redirect(url_for('account'))

    # parcels to render in 
    parcels = current_user.user_parcels
    states = []
    for key, value in models.storage.all("State").items():
        states.append(value)

    user_state = models.storage.ses().query(models.state.State).filter_by(name=current_user.user_state).first()
    user_city = models.storage.ses().query(models.city.City).filter_by(name=current_user.user_city).first()

    return render_template("account.html", profile_form=profile_form, create_form=create_form, parcels=parcels, contactus=contactus, states=states,
                            user_state=user_state, user_city=user_city)
