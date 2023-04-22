from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(20), unique=True, nullable=False)
    displayName = db.Column (db.String(20), unique=False, nullable=False)
    email = db.Column (db.String(100), unique=True, nullable=False)
    password = db.Column (db.String(100), nullable=False)
    address = db.Column (db.String(250))
    
#test
def __init__(self, username, displayName, email, password):
    self.username = username
    self.displayName = displayName
    self.email = email
    self.password = password

def create_password(self, password):
    self.password = generate_password_hash(password, method='sha256')

def check_password(self, password):
    return check_password_hash(self.password, password)
