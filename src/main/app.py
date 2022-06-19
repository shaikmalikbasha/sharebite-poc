import logging

import coloredlogs
from flask import Flask
from flask_restful import Api
from src.main.config import env_vars
from src.main.config.lib_instance import db, ma
from src.main.models.output_mixin import CustomJSONEncoder
from src.main.resources import section_resource, item_resource, modifier_resource

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG")

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../../database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma.init_app(app)

api = Api(app)


@app.before_first_request
def create_tables():
    logging.info("Initializing the database...")
    # db.drop_all()
    db.create_all()
    logging.info("All DB tables were successfully created!")


@app.route("/")
def index():
    """
    Root API: "/"
    Return:
        Basic details of the project
    """
    logging.info("Root API '/' called...")

    return {"success": True, "status_code": 200, "app_name": env_vars.APP_NAME}


api.add_resource(section_resource.SectionResourceList, "/api/v1/sections")
api.add_resource(item_resource.ItemResourceList, "/api/v1/items")
api.add_resource(modifier_resource.ModifierResourceList, "/api/v1/modifiers")
