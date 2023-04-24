import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
import click, sys
from flask_login import LoginManager, current_user
from App.views import views
from flask_migrate import Migrate
from App.db import *
from .controllers import flask_login, authenticate


#moved to db.py db = SQLAlchemy()

#add views
def addviews(app):
    for view in views:
        app.register_blueprint(view)

def create_app():
    
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="testkey",
        SQLALCHEMY_DATABASE_URI="sqlite:///database.db",
        #DATABASE=os.path.join(app.instance_path, "sqlite:///database.db"),  #check?
    )

    #views
    addviews(app)
    db.init_app(app)   #works here
    
    #moved to db.py : migrate = Migrate(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    authenticate(app)
    flask_login(app)
        
    with app.app_context():   #works here
        db.create_all()
    
    

    @app.route('/')
    def test():
        return 'Welcome to Tail!'

    return app

if __name__ == '__main__':
    app.run(debug=True)