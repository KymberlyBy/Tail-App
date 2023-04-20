from flask import Blueprint    

views = Blueprint('views', __name__)

#home
@views.route('/')
def mainPage():
    return "<h1>Hello User</h1>"