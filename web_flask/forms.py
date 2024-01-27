""" Forms used """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from web_flask import bycpt



class RegisterForm(FlaskForm):
    # Register form class
    full_name = StringField('Full name', validators=[DataRequired(), Length(min=3, max=60)])
    city = StringField('City', validators=[DataRequired(), Length(min=3, max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=124)])
    phone = StringField('Phone number', validators=[DataRequired(), Length(min=3, max=20)])
    postal_code = StringField('Postal code', validators=[DataRequired(), Length(min=3, max=20)])
    birth_date = DateField('Date of Birth')
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), Length(min=6), EqualTo('password')])
    submit = SubmitField('Register')

    # costum validation
    def validate_email(self, email):
        from models import storage
        user = storage.user_eamil(email.data)
        if user:
            raise ValidationError("Email already exist")


class LoginForm(FlaskForm):
    # Login form class
    email = StringField('Email', validators=[DataRequired(), Email()])  # Correct function name
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    rememberme = BooleanField('Remember me')
    submit = SubmitField('Log in')

    def validate_email(self, email):
        from models import storage
        user = storage.user_eamil(email.data)
        if not user:
            raise ValidationError("Email doesn't exist")
        
    def validate_password(form, password):
        from models import storage
        user = storage.user_eamil(form.email.data)
        if not user:
            raise ValidationError("Email doesn't exist")
        print(user)
        passw = user.user_password
        if not bycpt.check_password_hash(user.user_password, password.data):
            raise ValidationError('Wrong password')


