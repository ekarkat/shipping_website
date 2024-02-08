import os
from flask import Flask, render_template, url_for, request
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
import requests
from flask_mail import Mail



app = Flask(__name__)
app.config['SECRET_KEY'] = '6e8a95d08da92b8fb4158cc3ba66a6e5'
bycpt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)


@login_manager.user_loader
def load_user(user_id):
    from models import storage
    user = storage.user_id(user_id)
    return (user)


@app.before_request
def refresh_session():
    from models import storage
    storage.close()
    storage.reload()


from web_flask.routes.register import register
from web_flask.routes.commun import *
from web_flask.routes.login import *
from web_flask.routes.account import *
from web_flask.routes.test import *
from web_flask.routes.pwd_reset import *
