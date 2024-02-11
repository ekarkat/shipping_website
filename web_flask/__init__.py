from flask import Flask, render_template, url_for, request
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

app.config['SECRET_KEY'] = '6e8a95d08da92b8fb4158cc3ba66a6e5'
bycpt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

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
from web_flask.routes.dist import *
