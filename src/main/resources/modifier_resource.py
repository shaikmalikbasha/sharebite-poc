import logging

from flask_restful import Resource
from src.main.models.modifier_model import Modifier


class ModifierResource(Resource):
    pass


class ModifierResourceList(Resource):
    def get(self):
        modifiers = [modifier.to_json() for modifier in Modifier.find_all()]
        logging.info(modifiers)
        return {"modifiers": modifiers}
