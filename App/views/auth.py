from flask import Blueprint, redirect, render_template, jsonify, request
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from App.controllers import find_user, find_user_by_id, authenticate, authenticate_user, new_user, user_login

auth_view = Blueprint('auth_view', __name__, static_folder="static", template_folder="templates") #double check the '' here if errors come up

@auth_view.route('/login', methods=['POST'])
def userLogin():
    userInfo = request.form
    user = login(userInfo['username'], userInfo['password'])
    if user:
        login_user(user)
        return "Logged in successfully."
    return "Username and/or password was incorrect.", 401

@auth_view.route('/api/login', methods=['POST'])
def userLoginAPI():
    userInfo = request.json
    token = authenticate_user(userInfo['username'], userInfo['password'])
    if not token:
        return jsonify(message='username or password is incorrect'), 401
    return jsonify(accessToken=token)

@auth_view.route('/logout', methods=['GET'])
def userLogout():
    userInfo = request.form
    user = login(userInfo['username'], userInfo['password'])
    if user:
        logout_user(user)
        return "Logout successful."


@auth_view.route('/auth')
def login():
    return "this is a test."