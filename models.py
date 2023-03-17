from email.policy import default
from enum import unique
from datetime import datetime

from tomlkit import date
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(90))#, unique=True)
    points = db.Column(db.Integer)
    notes = db.relationship('Note')
 
