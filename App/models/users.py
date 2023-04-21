from flask import Flask, db

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(20), unique=True, nullable=False)
    displayName = db.Column (db.String(20), unique=False, nullable=False)
    email = db.Column (db.String(100), unique=True, nullable=False)
    password = db.Column (db.String(100), nullable=False)
    address = db.Column (db.String(250))
    

