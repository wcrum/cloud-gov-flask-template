from flask import Blueprint
from flask import request
from flask import jsonify

bp = Blueprint('debug', __name__)

@bp.route('/headers')
def debug_headers():
    _tmp = {}
    for h, v, in request.headers.items():
        _tmp[str(h)] = str(v)

    return jsonify(_tmp)