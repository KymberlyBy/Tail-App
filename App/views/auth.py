from flask import Blueprint, redirect, render_template

auth_view = Blueprint('auth_view', __name__, static_folder="static", template_folder="templates") #double check the '' here if errors come up

@auth_view.route('/auth')
def login():
    return "this is a test."