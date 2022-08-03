# imports and flask initialization
import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

# creates an instance of Flask called app
app = Flask(__name__)
# retrieves hidden env mongodb variable
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# retrieves hidden env postgres variable
# solves discrepancy between sqlalchemy requirement of using postgresql
# from with heroku's use of postgres in the config vars
uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

# assigns sqlalchemy app to variable called db
# assigns pymongo app to variable called mongo
db = SQLAlchemy(app)
mongo = PyMongo(app)

# imports routes from paleorecipes app
from paleorecipes import routes  # noqa
