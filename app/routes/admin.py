from flask import Blueprint
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
from flask import current_app
from app.utils.decorators import admin_required

bp = Blueprint("admin", __name__)

@bp.route("/")
@admin_required
def index():
    return render_template(
        "page.html", session=session, page=current_app.pages.unregistered_routes["admin.md"]
    )

@bp.route("/logs")
def logs():
    return render_template("log.html", sesssion=session)
