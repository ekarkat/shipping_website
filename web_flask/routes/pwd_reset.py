#!/usr/bin/python3
"""Reset password form route"""

from flask import render_template, url_for, request, flash, redirect
from web_flask import app, bycpt, mail
from web_flask.forms import RequestResetForm, RequestPasswordForm
from flask_login import current_user
from flask_mail import Message


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender="shipitletus@gmail.com",
                  recipients=[user.user_email])
    
    msg.body = f'''
    To reset your password, visit the following link
{url_for('reset_token', token=token, _external=True)}

if you did not make this request then simply ignore this email
'''
    mail.send(msg)



@app.route("/reset_pwd", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    # submit on validate conditional to handle the form being submited
    if form.validate_on_submit():
        from models import storage
        user = storage.user_by_email(form.email.data)
        send_reset_email(user)
        flash('An email has been sent to your address with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('pwd_reset_request.html', title='Reset Password', form=form)

@app.route("/reset_request/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    from models.user import User
    user = User.verify_reset_token(token)
    if not user:
        flash('Invalid or Expired Token', 'warning')
        return redirect(url_for(reset_request))
    form = RequestPasswordForm()
    if form.validate_on_submit():
        from models.user import User
        hashed_pass = bycpt.generate_password_hash(form.password.data).decode("utf-8")
        setattr(user, "user_password", hashed_pass)
        user.save()
        flash('Your password has been updated! You are now able to login')
        return render_template("home.html")
    return render_template('reset_token.html', title='Reset Password', form=form)

