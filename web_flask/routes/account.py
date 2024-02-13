#!/usr/bin/python3
"""Account rout"""
from flask import render_template, url_for, flash, request, redirect
from web_flask import app, mail
from flask_login import login_user, login_required, current_user
from web_flask.forms import CreateParcel, UserProfile, ContactUs
import models
from flask_cors import CORS
from flask_mail import Message


CORS(app, origins="0.0.0.0")

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
        user_dic = {
            "user_full_name" : profile_form.full_name.data,
            "user_email" : profile_form.email.data,
            "user_city" : profile_form.city.data,
            "user_address" : profile_form.address.data,
            "user_birth_date" : profile_form.birth_date.data,
        }

        user.update(**user_dic)
        user.save()

    if contactus.validate_on_submit():
        # if user submit in edit profile
        import os
        recipient = [os.environ.get('EMAIL_USER')]
        sender = contactus.email.data
        msg = Message('Contact us',
                      sender=sender,
                      recipients=recipient)
        msg.body = f"""message from : {sender}
content: 
{contactus.message.data}
"""
        mail.send(msg)  # assuming you have instantiated the Mail object as 'mail'
        flash('Your message has been sent!', 'success')
        print(contactus.message.data)
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

    # parcels to render in 
    parcels = current_user.user_parcels

    return render_template("account.html", profile_form=profile_form, create_form=create_form, parcels=parcels, contactus=contactus)
