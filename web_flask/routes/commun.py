#!/usr/bin/python3
"""Registarion form rout"""
from flask import render_template, url_for, request, redirect


from web_flask import app


@app.route("/")
def home():
    from models import storage
    total_shipments = storage.count_parcels()
    total_clients = storage.count_users()
    return render_template("home.html", total_shipments=total_shipments, total_clients=total_clients, title='Shipit')
from flask import Flask, render_template

@app.route('/service/')
def service():
    return render_template('service.html', title='Services')
@app.route('/About_us/')
def about_us():
    return render_template('About.html', title='About')
