""" imports """
from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from paleorecipes import app, db, mongo
from paleorecipes.models import Category, Recipe, User


@app.route("/")
def home():
    return render_template("index.html")




# @app.route("/profile/<username>", methods=["GET", "POST"])
# def profile(username):
#     return render_template("profile.html")
