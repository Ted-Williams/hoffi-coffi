import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    return render_template('pages/homepage.html', homepage=homepage)
    

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This allows the user to log in to
    the app using their username and password
    """
    if request.method == "POST":
        users = mongo.db.users.find_one(
            {'name' : request.form.get['login']})

        if user:
            if check_password_hash(users["password"],
            request.form.get("password")):
            

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for('login'))

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for('login'))

    return render_template('pages/login.html')


@app.route("/logout")
def logout():
    """
    Retuns the user back to the hompage when logged
    out
    """
    session.clear()
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

