import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.views import views
#from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="testkey",
        SQLALCHEMY_DATABASE_URI="sqlite:///database.db",
        #DATABASE=os.path.join(app.instance_path, "sqlite:///database.db"),  #check?
    )
    db.init_app(app)   #works here

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #migrate = Migrate(app,db) #in case of column changes. column name change, table name changes do not apply!

    with app.app_context():   #works here
        db.create_all()

    @app.route('/')
    def test():
        return 'this is a sample!'

    return app


        
 


   

if __name__ == '__main__':
    app.run(debug=True)