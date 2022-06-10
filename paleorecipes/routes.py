""" imports """
from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from paleorecipes import app, db, mongo
from paleorecipes.models import Category, Recipe, User


@app.route("/")
def home():
    """ Renders Home page"""
    return render_template("index.html")


# HANDLE REGISTER, CREATE PROFILE, LOGIN AND LOGOUT
@app.route("/register", methods=["GET", "POST"])
def register():
    """
        Check if user is already logged in, if so redirect user
        to the profile page. Get user's username from the form,
        check if it already exists in the database.
        If it does, flash a message to the user and redirect
        to the registration page. Check if passwords match and
        in the correct format. Save user in the database, put user
        into session cookie and redirect to profile page.
    """
    if "user" in session:
        return redirect(url_for('profile'))

    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(User.user_name == \
                                          request.form.get
                                          ("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = User(
            user_name=request.form.get("username").lower(),
            firstname=request.form.get("firstname"),
            password=generate_password_hash(request.form.get("password")),
        )

        db.session.add(user)
        db.session.commit()

        # add user profile to mongodb
        user_profile = {
            "avatar_no": int(request.form.get("avatar_no")),
            "fave_recipes": [],
            "my_recipes": [],
            "my_blog": [],
        }
        mongodb.users.insert_one(user_profile)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("firstname")
        flash ("Registration successful!")
        return redirect(url_for("profile", firstname=session["user"]))

    return render_template("register.html")










@app.route("/profile")
def profile():
    return render_template("profile.html")
