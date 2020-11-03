import os
import requests
from flask import (
    Flask, request, flash, render_template,
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    reviews = list(mongo.db.reviews.find())
    return render_template("index.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    try:
        searchterm = request.form.get('searchbox')
        URL = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm
        r = requests.get(url=URL)
        data = r.json()
        return render_template("results.html", data=data)

    except:
        return render_template("error.html")
    else:
        return render_template("results.html", data=data)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.username.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect login details")
                return redirect(url_for("login"))

        else:
            flash("Incorrect login details")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/search_review", methods=["GET", "POST"])
def search_review():
    profile_review_search = request.form.get("profile_review_search")
    reviews = list(mongo.db.reviews.find(
        {"$text": {"$search": profile_review_search}}))
    return render_template("profile.html", reviews=reviews)


@app.route("/logout")
def logout():
    flash("You've successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "book_name": request.form.get("book_name"),
            "user_review": request.form.get("user_review"),
            "genre_name": request.form.getlist("genre_name"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your review has been added!")
        return redirect(url_for("index"))

    genre = mongo.db.genre.find().sort("genre_name", -1)
    return render_template("add_review.html", genre=genre)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "book_name": request.form.get("book_name"),
            "user_review": request.form.get("user_review"),
            "genre_name": request.form.getlist("genre_name"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Your review has been updated!")
        return redirect(url_for("index"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review, genre=genre)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review successfully deleted")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
