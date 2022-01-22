from flask import Blueprint
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
from flask import current_app

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    print(session)
    return render_template("index.html", 
        sesssion = session
    )

@bp.after_request
def after_request(response):
    return response