from flask import Blueprint, request, render_template, flash, redirect, url_for, Flask
from importlib_metadata import metadata
from requests import session
from sqlalchemy import desc
from .models import User
from . import db
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user

user = Blueprint('user', __name__)

@user.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@user.route("/create", methods=["GET", "POST"])
def create():
    the_name = None
    form = User()
    if request.method == "POST":
        name = request.form.get('Name')
        #id = request.form.get('ID')
        points = request.form.get('Points')
        the_user = User.query.filter_by(name=name).first()
        if the_user:
            flash("User already exists!", category='error')

        elif len(name) < 4:
            flash("Name length must be more than 4 characters.", category='error')
        else:
            new_user = User(name=name, points=points)

            db.session.add(new_user)
            db.session.commit()
            flash("User created!", category='success')

            login_user(new_user, remember=True)
#            our_user = User.query()

            #return redirect(url_for('views.home'))

    user = User.query.all()
    return render_template("create.html", user=user)
        #elif not isinstance(id, int):
        #    flash("ID must be a number.", category='error')
        #elif not isinstance(points, int):
        #    flash("Points must be a number.", category='error')
    


@user.route("/display", methods=["GET", "POST"])
@login_required
def display():
    user = User.query.all()
    return render_template("display.html", users=user)



@user.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        form = request.form
        search_value = form["search_string"]
        search = "%{}%".format(search_value)
        result = User.query.filter(User.name).all()
        return render_template("search.html")
    else:
        return redirect(url_for("views.home"))
    

