from flask import Blueprint
from flask import request
from flask import jsonify

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return "This is an example app on cloud.gov!"