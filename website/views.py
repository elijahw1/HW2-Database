from unicodedata import category
from flask import Blueprint, flash, request, jsonify
from flask import render_template
from flask_login import current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    """if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note invalid", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added", category='success')
    """
    return render_template("home.html")

@views.route('/delete-user', methods=['POST'])
def delete_user():
    user = json.loads(request.name)
    userId = user['user']
    user = User.query.get(userId)
    if user:
        db.session.delete(user)
        db.session.commit()
    return jsonify({})