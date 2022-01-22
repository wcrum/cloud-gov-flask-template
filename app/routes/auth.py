import os
import jwt
import requests
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import redirect
from flask import current_app
from flask import session
from urllib.parse import unquote
from base64 import b64encode

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    CLIENT_ID = current_app.config["CLIENT_ID"]
    REDIRECT_URI = current_app.config["REDIRECT_URI"]
    USER_STATE = b64encode(os.urandom(64)).decode("utf-8")
    UAA_AUTHORIZE_URI = current_app.config["UAA_AUTHORIZE_URI"]

    session["USER_STATE"] = USER_STATE
    
    UAA_LOGIN = f"{UAA_AUTHORIZE_URI}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&state={USER_STATE}"
    
    return redirect(UAA_LOGIN)

@bp.route('/logout')
def logout():
    CLIENT_ID = current_app.config["CLIENT_ID"]
    REDIRECT_URI = current_app.config["REDIRECT_URI"]
    UAA_LOGOUT_URI = current_app.config["UAA_LOGOUT_URI"]
    UAA_LGOUT = f"{UAA_LOGOUT_URI}?client_id={CLIENT_ID}&redirect={REDIRECT_URI}"

    session.clear()
    requests.post(UAA_LGOUT)
    
    return redirect("/")

@bp.route('/callback')
def callback():
    # @url_param {string} code
    # @url_param {string} status
    code = request.args.get('code')
    state = request.args.get('state')
    
    UAA_TOKEN_URI = current_app.config["UAA_TOKEN_URI"]

    data = {
        "code": code,
        "grant_type": "authorization_code",
        "response_type": "token",
        "client_id": current_app.config["CLIENT_ID"],
        "client_secret": current_app.config["CLIENT_SECRET"],
        "redirect_uri": current_app.config["REDIRECT_URI"]
    }

    response = requests.post(
        UAA_TOKEN_URI,
        data = data
    ).json()

    token = response["access_token"]
    header = jwt.get_unverified_header(token)

    session["claims"] = jwt.decode(token, header["alg"], options={"verify_signature": False})
    session["expiry"] = response["expires_in"]
    session["refresh_token"] = response["refresh_token"]
    session["authenticated"] = True

    return redirect('/')