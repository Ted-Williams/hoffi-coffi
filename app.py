import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask (__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def homepage():
    """
    Function which takes the user to the 
    homepage when the app loads
    """
    return render_template('pages/homepage.html')


app.route("/login", methods=["GET", "POST"])
def log_in():
    """
    This allows the user to log in to
    the app using their username and password
    """
    return render_template('pages/login.html')


@app.route("/logout")
def logout():
    return render_template('pages/homepage.html')

@app.route("/admin/<user_id>")
def admin():
    return render_template('pages/admin.html')


@app.route("/coffee")
def coffee():
    return render_template('pages/coffee.html')



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

