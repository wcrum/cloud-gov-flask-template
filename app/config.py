import os
import urllib

class Config(object):
    TESTING = False

class Production(Config):
    PORT = 8080

    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    REDIRECT_URI = "https://template-flask-usmc.app.cloud.gov/auth/callback"
    LOGOUT_REDIRECT_URI = "https://template-flask-usmc.app.cloud.gov/"
    UAA_AUTHORIZE_URI = "https://login.fr.cloud.gov/oauth/authorize"
    UAA_LOGOUT_URI = "https://login.fr.cloud.gov/logout"
    UAA_TOKEN_URI = "https://uaa.fr.cloud.gov/oauth/token"

    # state is an important to prevent CSRF, this is temporyr

class Testing(Config):
    TESTING = True
    HOST = "localhost"
    PORT = 8000

    CLIENT_ID = "my_client_id"
    CLIENT_SECRET = "my_client_secret"
    REDIRECT_URI = f"http://localhost:{PORT}/auth/callback"
    UAA_AUTHORIZE_URI = "http://localhost:8080/oauth/authorize"
    LOGOUT_REDIRECT_URI = f"http://localhost:{PORT}/"
    UAA_LOGOUT_URI = "http://localhost:8080/logout"
    UAA_TOKEN_URI = "http://localhost:8080/oauth/token"