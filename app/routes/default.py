from flask import Blueprint
from flask import request
from flask import jsonify
from flask import session

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    if session.get("authenticated"):
        return "You are authenticated!"
    return "This is an example app on cloud.gov!"

@bp.after_request
def after_request(response):
    return response