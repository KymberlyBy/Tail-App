from flask import Blueprint, render_template

bp = Blueprint ("auth", __name__, url_prefix="/auth")