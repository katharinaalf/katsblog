import os
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
### line above is getting the absolute path to where my file is located - this is where you build database###

app = Flask(__name__)
 
##connect flask application to database  'sqlite:///'+os.path.join(basedir, 'data.sqlite')##

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

######### setting up  the first model #######

class Userdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.name} email address is {self.email}"

