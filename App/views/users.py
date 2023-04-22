from flask import Blueprint, redirect, render_template

users_view = Blueprint('users_view', __name__, static_folder="static", template_folder="templates")

@users_view.route("/testusers")
def testuser():
    render_template("users_template.html")
    #return "hello! this is the /testusers sample page!"