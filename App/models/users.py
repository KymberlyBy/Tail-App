from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import json

db = SQLAlchemy()

#removed nullable properties from: firstName, lastName, email, home_address [temp]
class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(20), unique=True, nullable=False)
    firstName = db.Column (db.String(20), unique=False)
    lastName = db.Column (db.String(20), unique=False)
    email = db.Column (db.String(100), unique=True)
    password = db.Column (db.String(100), nullable=False)
    home_address = db.Column (db.String(250))
    home_latitude = db.Column (db.DOUBLE_PRECISION)
    home_longtitude = db.Column (db.DOUBLE_PRECISION)
    
#test
def __init__(self, id,  username, firstName, lastName, email, password, home_address, home_latitude, home_longtitude):
    self.id = id
    self.username = username
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.password = password
    self.home_address = home_address
    self.home_latitude = home_latitude
    self.home_longtitude = home_longtitude  

def create_password(self, password):
    self.password = generate_password_hash(password, method='sha256')

def check_password(self, password):
    return check_password_hash(self.password, password)

def get_json(self):
    return {
        "ID": self.id,
        "Username": self.username,
        "First Name": self.firstName,
        "Last Name": self.lastName,
        "Email": self.email,
        "Home Address": self.home_address  #no lat and long atm
    }

