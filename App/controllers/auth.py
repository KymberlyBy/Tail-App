from flask_login import login_user, logout_user, login_manager, LoginManager
from flask_jwt_extended import jwt_required, create_access_token, JWTManager

from App.models import User

def user_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

def authenticate_user(username, password):
    user=User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return create_access_token(identity=username)
    return None  


def flask_login(app):
    loginManager = LoginManager()
    loginManager.init_app(app)
    @loginManager.user_loader 
    def getUser(id):
        return User.query.get(id)
    return loginManager

def authenticate(app):
    auth = JWTManager(app)

    @auth.user_identity_loader
    def userIDLookup(identity):
        user = User.query.filter_by(username=identity).one_or_none()
        if user:
            return user.id 
        return None

    @auth.user_lookup_loader
    def userLookup(_jwt_header, jwt_data):
        id = jwt_data["sub"]
        return User.query.get(id)

    return auth            
    

