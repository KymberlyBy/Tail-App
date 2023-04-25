from flask import Blueprint, redirect, render_template, jsonify, request
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from App.controllers import find_user, find_user_by_id, authenticate, authenticate_user, new_user


users_view = Blueprint('users_view', __name__, static_folder="static", template_folder="templates")







@users_view.route("/testusers")
def testuser():
    return render_template("users_template.html")
    #return "hello! this is the /testusers sample page!"