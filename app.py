import os 
import json
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
    return render_template('pages/homepage.html', homepage=homepage, loggedOut=1)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This allows the user to log in to
    the app using their username and password
    """
    
    if request.method == "POST":
        user = mongo.db.users.find_one({'email' : request.form.get('email')})
        if user:
            #if check_password_hash(user["password"],
            #request.form.get("password")):
            if user['password'] == request.form.get('password'):
                session["users"] = request.form.get("email").lower()
                flash("Welcome, {}".format(request.form.get("email")))
                return redirect(url_for("admin", user_id=user["_id"]))

        else:
            print("Incorrect username and/or password")
            return redirect(url_for('login'))

    else:
        flash("Incorrect username and/or password")
        #return redirect(url_for('logo'))

    return render_template('pages/login.html')

@app.route("/logout")
def logout():
    """
    Retuns the user back to the hompage when logged
    out
    """
    session.clear()
    return render_template('pages/homepage.html')

@app.route("/admin/<user_id>", methods=["GET", "POST"])
def admin(user_id):
    """
    Shows the user that they are logged in 
    and are able to add/delete a coffee
    """
    coffeeList = mongo.db.coffee.find({})
    formattedCoffeeList = []
    for coffee in list(coffeeList):
        coffee['_id'] = str(coffee['_id'])
        formattedCoffeeList.append(coffee)
    if request.method == "GET":
        return render_template('pages/admin.html', coffeeList=list(formattedCoffeeList), loggedIn=1)
    else:
        coffee_id = request.form.get('coffeeControl')
        return redirect(url_for("adminEditCoffee", user_id=user_id, coffee_id=coffee_id))

@app.route("/admin/<user_id>/<coffee_id>", methods=["GET", "POST"])
def adminEditCoffee(user_id, coffee_id):
    """
    Shows the user that they are logged in 
    and are able to add/delete a coffee
    """
    if request.method == "GET":
        coffee = mongo.db.coffee.find_one({"_id": ObjectId(coffee_id)})
    return render_template('pages/admin-edit.html', coffee=coffee, loggedIn=1)

@app.route("/edit/coffee")
def coffee():
    """
    shows the static coffee page to all users
    """
    return render_template('pages/coffee.html')

@app.route("/forward")
def move_forward():
    print("Moving Forward...")
    return render_template('pages/homepage.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

