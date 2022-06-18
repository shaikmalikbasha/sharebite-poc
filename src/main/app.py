import logging

import coloredlogs
from flask import Flask
from flask_restful import Api
from src.main.config.lib_instance import db

from src.main.config import env_vars

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

api = Api(app)


@app.route("/")
def index():
    """
    Root API: "/"
    Return:
        Basic details of the project
    """
    logging.info("Root API '/' called...")

    return {"success": True, "status_code": 200, "app_name": env_vars.APP_NAME}
