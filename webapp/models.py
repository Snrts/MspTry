
from soupsieve import select
from . import db 
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course1 = db.Column(db.String(150))
    course2 = db.Column(db.String(150))
    skill = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #store a foreign key on the child objects that reference the parent object
    #forms the relationship between the person adding the course and the choice

class User(db.Model, UserMixin): #lets us inherit from both #using uppercase is python standard but we reference them in SQL with lowercase
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname= db.Column(db.String(150))
    lastname= db.Column(db.String(150))
    select = db.relationship('Note') #tells flask and SQLalchemy to add the courses to a users account (adds a list to the user)

class Course(db.Model):
    code = db.Column(db.String(3))
    nr = db.Column(db.Integer)
    tag_label = db.Column(db.String(2), db.ForeignKey('tag.label'))
    tag_period= db.Column(db.String(2), db.ForeignKey('tag.period'))

    def __init__(self, code, nr):
        self.id = code+nr

class Tag(db.Model):
    period = db.Column(db.Integer, primary_key=True)
    label = db.relationship('Course')
    
