from flask import Flask



def create_app():
    app = Flask(__name__)

    #database set up
    from . import db
    db.init_app(app)


    return app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  