import werkzeug
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
from flask import current_app
from werkzeug.exceptions import HTTPException
from flask import json

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


@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    if (handle_error:= request.headers.get("X-Error-Type")) == "JSON":
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response, e.code
    else:
        return render_template(
            "404.html",
            error = e
        )