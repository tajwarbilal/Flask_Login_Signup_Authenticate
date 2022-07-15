from flask import Blueprint, render_template

home_blueprints = Blueprint('home_blueprints', __name__)


@home_blueprints.route('/')
def home():
    return render_template('home.html')
