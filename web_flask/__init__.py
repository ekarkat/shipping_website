from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)
from web_flask.route.register import register
from web_flask.route.commun import *