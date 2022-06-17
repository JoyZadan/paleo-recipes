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
        @login_required decorator -
        https://flask.palletsprojects.com/en/2.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to be logged in to view this page")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/get_recipes")
def get_recipes():
    """ docstrings """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/get_categories")
def get_categories():
    """ docstrings """
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories of recipes!")
        return redirect(url_for("get_recipes"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


# HANDLE REGISTER, LOGIN, LOGOUT, AND CREATE PROFILE
@app.route("/register/", methods=["GET", "POST"])
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
            firstname=request.form.get("firstname").lower(),
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
            "fave_recipes": [],
            "my_recipes": [],
            "my_blog": []
        }

        mongo.db.users.insert_one(user_profile)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))

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
    """ remove user from session cookie """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """
        Query Postgres
        Get user's profile from MongoDB
        Get user's input for all fields and render on profile page
    """
    if "user" in session:
        return render_template("profile.html", username=session["user"])
    return redirect(url_for("login"))
