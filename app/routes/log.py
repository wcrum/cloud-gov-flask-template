from flask import Blueprint
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
from flask import current_app

bp = Blueprint("admin", __name__)


@bp.route("/logs")
def index():
    return render_template("log.html", sesssion=session)
