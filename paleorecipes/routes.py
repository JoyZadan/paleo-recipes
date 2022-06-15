""" imports """
from functools import wraps
from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from paleorecipes import app, db, mongo
from paleorecipes.models import Category, Recipe, Users


@app.route("/")
def home():
    """ Renders Home page"""
    return render_template("index.html")


def login_required(f):
    """
        Ensures page us only accessible to logged in users
        @login_required decorator - https://flask.palletsprojects.com/en/2.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to be logged in to view this page")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# HANDLE REGISTER, CREATE PROFILE, LOGIN AND LOGOUT
@app.route("/register", methods=["GET", "POST"])
def register():
    """
        Check if user is already logged in, if so redirect user
        to the profile page. Get user's username from the form,
        check if it already exists in the database.
        If it does, flash a message to the user and redirect
        to the registration page. Save user in postgres db,
        insert user_profile in mongodb, put user
        into session cookie and redirect to profile page.
    """
    if "user" in session:
        return redirect(url_for('profile'))

    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(Users.user_name ==
                                          request.form.get
                                          ("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password")),
        )

        db.session.add(user)
        db.session.commit()

        # query postgres db to get the id of the new user
        # get and save the id of the new user into a variable
        # pass said id to user_id as a string in MongoDB
        # MongoDB by default saves the user id as a string
        # according to Code Institute's combining databases lesson 2
        new_user = Users.query.get_or_404(user.id)

        # add user profile to mongodb
        user_profile = {
            "user_id": str(new_user.id),
            "firstname": str(request.form.get("firstname")),
            "avatar_no": int(request.form.get("avatar_no")),
            "fave_recipes": [],
            "my_recipes": [],
            "my_blog": []
        }

        mongo.db.users.insert_one(user_profile)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("firstname")
        flash ("Registration successful!")
        return redirect(url_for("profile", firstname=session["user"]))

    return render_template("register.html")


# from Code Institute combined databases source code
# amended for my requirements
@app.route("/login", methods=["GET", "POST"])
def login():
    """
        Check if user is already logged in, if so redirect user
        to the profile page. Get user's username from the form,
        check if it already exists in the database.
        If it does, flash a message to the user and redirect
        to the login page. Save user in postgres db,
        insert user_profile in mongodb, put user
        into session cookie and redirect to profile page.
    """
    if "user" in session:
        return redirect(url_for('profile'))
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(Users.user_name ==
                                           request.form.get(
                                            "username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<>", methods=["GET", "POST"])
@login_required
def profile():
    """
        Get user's firstname from MongoDB
        Get user's input for all fields and update in db.
    """
    if "user" not in session:
        return redirect(url_for('register'))

    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(Users.id ==
                                          request.form.get
                                          ("user.id").lower()).all()

    new_user = Users.query.get_or_404(user.id)

    user_profile = {
            "avatar_no": int(request.form.get("avatar_no")),
        }

    mongo.db.users_update_one(user_profile)


