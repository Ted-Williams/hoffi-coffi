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
    """
    Retuns the user back to the hompage when logged
    out
    """
    return render_template('pages/homepage.html')

@app.route("/admin/<user_id>")
def admin():
    """
    Shows the user that they are logged in 
    and are able to add/delete a coffee
    """
    return render_template('pages/admin.html')


@app.route("/coffee")
def coffee():
    """
    shows the static coffee page to all users
    """
    return render_template('pages/coffee.html')



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

