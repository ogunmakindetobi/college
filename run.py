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
DATABASE = "college"
COLLECTION = "courses"



@app.route('/')
@app.route('/get_courses')
def index():
    courses = list(mongo.db.courses.find())
    return render_template("index.html", courses=courses)

@app.route("/delete_course/<course_id>")
def delete_course(course_id):
    print(course_id)
    mongo.db.courses.delete_one({"_id": ObjectId(course_id)})
    print(mongo.db.courses.find_one({"_id": ObjectId(course_id)}))
    flash("Course successfully deleted")
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html", page_title='About')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
              request.form["name"]))

    return render_template("contact.html", page_title='Contact')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome,{}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))
    return render_template("login.html", page_title='login')


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # reomove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_course/add", methods=['GET', 'POST'])
def create_course():
    if request.method == "POST":
        courses = {
            "course_name": request.form.get("course_name"),
            "course_number": request.form.get("course_number"),
            "course_description": request.form.get("course_description"),
            "course_mark": request.form.get("course_mark"),
            "created_by": session["user"]
        }
        print(courses)
        mongo.db.courses.insert_one(courses)
        flash("Course Successfully Added")
        return redirect(url_for("index"))

    return render_template("create_course.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
    # check if username already exists in db
        print(request.form.get("username"))
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)