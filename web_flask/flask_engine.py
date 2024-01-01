#!/usr/bin/python3
"""Flask Model"""

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/about/")
# def about():
# 	return render_template("about.html")


data = []

@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("*********************** post request ******************** \n")
        print(request.form.get("full_name"))
        return render_template("home.html")
    if request.method == 'GET':
        print("\n \n \ n ******************* get method *************************")

    return render_template("register.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
