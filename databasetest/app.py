import os
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
### line above is getting the absolute path to where my file is located - this is where you build database###

app = Flask(__name__)
 
##connect flask application to database  'sqlite:///'+os.path.join(basedir, 'data.sqlite')##

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

######### setting up  the first model #######

class Userdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    usertype = db.Column(db.Text)
    resource = db.relationship('Resources', backref = 'user', uselist = False)

    def __init__(self, name, email, usertype):
        self.name = name
        self.email = email
        self.usertype = usertype

    def __repr__(self):
        if self.resource:
            return f"The resource for {self.name} is {self.resource.resource_type}"
        else: 
            return f"{self.name} has no resource yet!"

class Resources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    resource_type = db.Column(db.Integer, db.ForeignKey('Userdetails.id'))

    def __init__(self, user_type, resource_type):
        self.user_type = user_type
        self.resource_type = resource_type


if __name__ == '__main__':
    app.run()