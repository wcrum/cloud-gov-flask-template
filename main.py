import os
from flask import Flask

import os
import requests
from app import config
from app.routes import default
from app.routes import debug
from app.routes import auth

APP_SETTINGS = os.getenv("APP_SETTINGS", "Testing")

def create_app():

    app = Flask(
        __name__, 
        template_folder="app/templates/", 
        static_folder="app/static/"
    )
    
    app.config.from_object(f'app.config.{APP_SETTINGS}')
    app.secret_key = os.urandom(256)
    app.url_map.strict_slashes = False

    app.register_blueprint(default.bp)
    app.register_blueprint(debug.bp, url_prefix="/debug")
    app.register_blueprint(auth.bp, url_prefix="/auth")
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        host = app.config.get("HOST"),
        port = app.config.get("PORT")
    )