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
    coffeeList = mongo.db.coffee.find({})
    formattedCoffeeList = []
    for coffee in list(coffeeList):
        coffee['_id'] = str(coffee['_id'])
        formattedCoffeeList.append(coffee)
    return render_template('pages/homepage.html', coffeeList=list(formattedCoffeeList), loggedOut=1)
    
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
    added = request.args.get('added')
    if added: added = int(added)
    deleted = request.args.get('deleted')
    if deleted: deleted = int(deleted)
    coffeeList = mongo.db.coffee.find({})
    formattedCoffeeList = []
    for coffee in list(coffeeList):
        coffee['_id'] = str(coffee['_id'])
        formattedCoffeeList.append(coffee)
    if request.method == "GET":
        return render_template('pages/admin.html', coffeeList=list(formattedCoffeeList), loggedIn=1, user_id=user_id, added=added, deleted=deleted)
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
    return render_template('pages/admin-edit.html', coffee=coffee, loggedIn=1, user_id=user_id)

@app.route("/admin/update-coffee/<user_id>/<coffee_id>", methods=["GET", "POST"])
def adminUpdateCoffee(user_id, coffee_id):
    """
    Updates the database values with user input field data
    """
    if request.method == "POST":
        newValues = { "$set": {
            "product_name": request.form.get('coffeeName'),
            "price": request.form.get('price'),
            "origin": request.form.get('origin'),
            "taste": request.form.get('taste'),
            "image_url": request.form.get('image_url'),
        }}
        result = mongo.db.coffee.update_one({"_id": ObjectId(coffee_id)}, newValues)
        coffee = mongo.db.coffee.find_one({"_id": ObjectId(coffee_id)})
        if result:
            return render_template('pages/admin-edit.html', coffee=coffee, loggedIn=1, user_id=user_id, updated=1)
        else:
            return render_template('pages/admin-edit.html', coffee=coffee, loggedIn=1, user_id=user_id, updated=0)

@app.route("/admin/delete-coffee/<user_id>/<coffee_id>", methods=["GET", "POST"])
def adminDeleteCoffee(user_id, coffee_id):
    """
    Delete a database entry using coffee_id
    """
    result = mongo.db.coffee.delete_one({"_id": ObjectId(coffee_id)})
    if result and result.deleted_count:
        return redirect(url_for("admin", loggedIn=1, user_id=user_id, deleted=1))
    else:
        return redirect(url_for("admin", loggedIn=1, user_id=user_id, deleted=0))

@app.route("/admin/add-coffee/<user_id>", methods=["GET", "POST"])
def adminAddCoffee(user_id):
    """
    Insert a new database entry
    """
    if request.method == "GET":
        return render_template('pages/admin-add.html', loggedIn=1, user_id=user_id)
    else:
        product_name = request.form.get('coffeeName')
        if product_name: 
            newValues = {
                "product_name": product_name,
                "price": request.form.get('price'),
                "origin": request.form.get('origin'),
                "taste": request.form.get('taste'),
                "image_url": request.form.get('image_url'),
            }
            result = mongo.db.coffee.insert_one(newValues)
            if result and result.inserted_id:
                return redirect(url_for("admin", loggedIn=1, user_id=user_id, added=1))
            else:
                return redirect(url_for("admin", loggedIn=1, user_id=user_id, added=0))
        else:
            return render_template('pages/admin-add.html', loggedIn=1, user_id=user_id, missingName=1)


@app.route("/forward")
def move_forward():
    print("Moving Forward...")
    # return render_template('pages/admin-edit.html', coffee=coffee, loggedIn=1)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

