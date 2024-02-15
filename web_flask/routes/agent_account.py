#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, request, redirect, flash
from web_flask import app
from flask_login import login_user, login_required, current_user
from web_flask.forms import PickUp, UserProfile, ContactUs
import models


@app.route("/agent-account/", methods=["GET", "POST"])
@login_required
def agent_account():
    # Account route
    pickup_form = PickUp()
    profile_form = UserProfile()
    contactus = ContactUs()

    if profile_form.validate_on_submit():
        # if user submit in edit profile
        pass

    if contactus.validate_on_submit():
        # if user submit in edit profile
        return redirect(url_for('account'))

    if pickup_form.validate_on_submit():
        # if user create a parcel
        # from models.state import State
        # from models.city import City
        # state = models.storage.ses().query(State).filter_by(id=request.form['states']).first().name
        # city = models.storage.ses().query(City).filter_by(id=request.form['cities']).first().name
        if request.form['delivery_type'] == "pick":
            current_user.pickup(pickup_form.tracking_number.data)

        if request.form['delivery_type'] == "deliver":
            if models.storage.parcel_track(pickup_form.tracking_number.data) in current_user.agent_parcels:
                current_user.deliver(pickup_form.tracking_number.data)
                flash('Form submitted successfully!', 'success')

            else:
                print("False")
        # parcel = {
        #     "to_name" : create_form.to_name.data,
        #     "to_phone_number" : create_form.to_phone_number.data,
        #     "to_address" : create_form.to_address.data,
        #     "to_state" : state,
        #     "to_city" : city,
        #     "to_postalcode" : create_form.to_postalcode.data,
        #     "parcel_type" : request.form['parcel_type'],
        #     "parcel_cost" : create_form.parcel_cost.data,
        #     "parcel_weight" : create_form.parcel_weight.data,
        #     "parcel_comments" : create_form.parcel_comments.data,
        # }
        # # print(parcel)
        # current_user.create_parcel(**parcel)
        pass

    # parcels to render in 
    parcels = current_user.agent_parcels
    states = []
    for key, value in models.storage.all("State").items():
        states.append(value)

    agent_state = models.storage.ses().query(models.state.State).filter_by(name=current_user.agent_state).first()
    agent_city = models.storage.ses().query(models.city.City).filter_by(name=current_user.agent_city).first()

    return render_template("agent_account.html", profile_form=profile_form, pickup_form=pickup_form, parcels=parcels, contactus=contactus, states=states,
                            agent_state=agent_state, agent_city=agent_city)
