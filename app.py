import os
import requests
from flask import (
    Flask, request, flash, render_template,
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    searchterm = request.form.get('searchbox')
    URL = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm
    r = requests.get(url=URL)
    data = r.json()
    return render_template("results.html", data=data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
