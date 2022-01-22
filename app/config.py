import os
import urllib

class Config(object):
    TESTING = False

class Production(Config):
    PORT = 8080

class Development(Config):
    CLIENT_ID = os.getenv("client_id")
    REDIRECT_URI = urllib.parse.quote("https://template-flask-usmc.app.cloud.gov/auth/callback")
    # state is an important to prevent CSRF, this is temporyr
    UAA_LOGIN = f"https://login.fr.cloud.gov/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&state=9ab894ad91d99eb9ee4b30ea7f02b9d8e43eb15db58ff93e4894f3b49817d7ab"

    PORT = 8080

class Testing(Config):
    TESTING = True
    PORT = 5000