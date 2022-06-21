""" imports """
import os
from functools import wraps
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from paleorecipes import app, db, mongo
from paleorecipes.models import Category, Users


cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'),
                  api_key=os.getenv('API_KEY'),
                  api_secret=os.getenv('API_SECRET'))


@app.route("/")
def home():
    """ Renders Home page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """ Renders About page"""
    return render_template("about.html")


@app.route("/blog")
def blog():
    """ Renders Blog page"""
    return render_template("blog.html")


def login_required(f):
    """
        Ensures page is only accessible to logged in users
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


# HANDLE CREATE, READ, UPDATE, DELETE AND SEARCH RECIPES
# from Code Institute combined databases source code
# amended for my requirements
@app.route("/recipes")
def recipes():
    """ renders recipes on recipes page """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search_recipes", methods=["GET", "POST"])
def search_recipes():
    """ finds recipes from db and renders them on recipes page """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """
    checks if user is in session, if not, redirects them to login page
    handles Cloudinary image upload from users using a public API key
    which will be provided in the FAQ section
    adds to mongodb the new recipe upload by the user
    """
    if "user" not in session:
        flash("You must be logged in to add a recipe")
        return redirect(url_for("login"))

    if request.method == "POST":
        image = request.files["image_url"]
        image_upload = cloudinary.uploader.upload(image,
                                                  upload_preset="efjhsj")
        recipe = {
            "category_id": request.form.get("category_id"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "image_url": image_upload["secure_url"],
            "created_by": session["user"],
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "servings": request.form.get("servings"),
            "notes": request.form.get("notes"),
            "nutrition": request.form.get("nutrition")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you for sharing your recipe!")
        return redirect(url_for("recipes"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    checks if user is in session, if not, redirects them to login page
    allows a user to edit their own recipes
    updates the user's own recipe in mongodb
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if "user" not in session or session["user"] != recipe["created_by"]:
        flash("You must be logged in to edit only your own recipes!")
        return redirect(url_for("recipes"))

    if request.method == "POST":
        request.form.get("recipe_name")
        image = request.files["image_url"]
        image_upload = cloudinary.uploader.upload(image,
                                                  upload_preset="efjhsj")
        submit = {
            "category_id": request.form.get("category_id"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "image_url": image_upload["secure_url"],
            "created_by": session["user"],
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "servings": request.form.get("servings"),
            "notes": request.form.get("notes"),
            "nutrition": request.form.get("nutrition")
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                    {"$set": submit})
        flash("Recipe successfully updated!")
        return redirect(url_for("recipes"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("edit_recipe.html", recipe=recipe,
                           categories=categories)


@app.route("/delete_recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    """
    checks if user is in session, if not, redirects them to login page
    allows a user to delete their own recipes,
    deletes the recipe from mongodb
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if "user" not in session or session["user"] != recipe["created_by"]:
        flash("You must be logged in to edit your own recipes!")
        return redirect(url_for("recipes"))

    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


# HANDLE CREATE, READ, UPDATE AND DELETE CATEGORIES
# from Code Institute combined databases source code
# amended for my requirements
# full CRUD functionalities for superadmin user
@app.route("/categories")
@login_required
def categories():
    """
    checks if user is superadmin
    if not, user is redirected to recipes page
    """
    if "user" not in session or session["user"] != "superadmin":
        flash("You must be a superadmin to manage categories of recipes!")
        return redirect(url_for("recipes"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    """
    checks if user is superadmin
    if not, user is redirected to recipes page
    add categories
    """
    if "user" not in session or session["user"] != "superadmin":
        flash("You must be a superadmin to manage categories of recipes!")
        return redirect(url_for("get_recipes"))

    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        flash("New Category successfully added!")
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    """
        checks if user is superadmin
        if not, user is redirected to recipes page
        edit categories
    """
    if "user" not in session or session["user"] != "superadmin":
        flash("You must be a superadmin to manage categories of recipes!")
        return redirect(url_for("get_recipes"))

    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        flash("Category successfully edited!")
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
@login_required
def delete_category(category_id):
    """
        checks if user is superadmin
        if not, user is redirected to recipes page
        delete category
    """
    if session["user"] != "superadmin":
        flash("You must be a superadmin to manage categories of recipes!")
        return redirect(url_for("get_recipes"))

    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    mongo.db.recipes.delete_many({"category_id": str(category_id)})
    flash("Category successfully deleted!")
    return redirect(url_for("categories"))


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
            request.form.get("username")
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
    flash("You have been logged out. See you soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/", methods=["GET", "POST"])
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


# HANDLE ERRORS
# inspired by:
# https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application
# @app.route("/messages")
