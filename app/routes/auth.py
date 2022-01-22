from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect
from flask import current_app

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    return redirect(current_app.config["UAA_LOGIN"])

@bp.route('/callback')
def callback():
    return ""