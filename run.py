import os
from flask import (
    Flask, render_template, request, flash, 
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

    
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)



@app.route('/')
@app.route('/index')
def index():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)

@app.route("/about")
def about():
    return render_template("about.html", page_title='About')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
              request.form["name"]))

    return render_template("contact.html", page_title='Contact')

@app.route("/login")
def login():
    return render_template("login.html", page_title='Login')

@app.route("/loginform", methods=["GET", "POST"])
def loginform():
    print("username is {} and the password is {}".format(
        request.form["username"], request.form["password"]))
    return render_template("login.html", page_title='login')


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)