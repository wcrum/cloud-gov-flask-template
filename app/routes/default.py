import os
import time
import werkzeug
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
from flask import current_app
from flask import abort
from werkzeug.exceptions import HTTPException
from flask import json

bp = Blueprint("index", __name__)


@bp.route("/")
@bp.route("/<path:path>")
def handle_posts(*args, **kwgs):
    if request.path in current_app.pages.routes:
        return render_template(
            "page.html",
            session=session,
            page=current_app.pages.routes[request.path]
        )

    abort(404)


@bp.before_request
def before_request():
    if session.get("expiry"):
        if time.time() > session.get("expiry"):
            # @url_param {string} code
            # @url_param {string} status
            UAA_TOKEN_URI = current_app.config["UAA_TOKEN_URI"]

            data = {
                "grant_type": "refresh_token",
                "refresh_token": session.get("refresh_token"),
                "client_id": current_app.config["CLIENT_ID"],
                "client_secret": current_app.config["CLIENT_SECRET"],
            }

            response = requests.post(UAA_TOKEN_URI, data=data).json()

            token = response["access_token"]
            header = jwt.get_unverified_header(token)

            session["claims"] = jwt.decode(
                token, header["alg"], options={"verify_signature": False}
            )
            session["expiry"] = time.time() + (response["expires_in"] * 1000)
            session["refresh_token"] = response["refresh_token"]
            session["authenticated"] = True


@bp.after_request
def after_request(response):
    print(session.get("expiry"), flush=True)
    return response


@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    if (handle_error := request.headers.get("X-Error-Type")) == "JSON":
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response, e.code
    else:
        return render_template("error.html", error=e)
