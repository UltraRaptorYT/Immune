from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(100))

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer)
    cough = db.Column(db.Integer)
    muscle_aches = db.Column(db.Integer)
    tiredness = db.Column(db.Integer)
    sore_throat = db.Column(db.Integer)
    runny_nose = db.Column(db.Integer)
    stuffy_nose = db.Column(db.Integer)
    fever = db.Column(db.Integer)
    nausea = db.Column(db.Integer)
    vomiting = db.Column(db.Integer)
    diarrhea = db.Column(db.Integer)
    shortness_of_breath = db.Column(db.Integer)
    difficulty_breathing = db.Column(db.Integer)
    loss_of_taste = db.Column(db.Integer)
    loss_of_smell = db.Column(db.Integer)
    itchy_nose = db.Column(db.Integer)
    itchy_eyes = db.Column(db.Integer)
    itchy_mouth = db.Column(db.Integer)
    itchy_inner_ear = db.Column(db.Integer)
    sneezing = db.Column(db.Integer)
    pink_eye = db.Column(db.Integer)
    prediction = db.Column(db.Integer)
    predicted_on = db.Column(db.DateTime, nullable=False)
