import os
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
### line above is getting the absolute path to where my file is located - this is where you build database###

app = Flask(__name__)
 
##connect flask application to database##

app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

######### setting up  the first model #######

class Userdetails(db.Model):
    __tablename__: 'User Details'

id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.Text)
email = db.Column(db.Text)

def __init__(self, name, email):
    self.name = name
    self.email = email

def __repr__(self):
    return f"{self.name} email address is {self.email}"

