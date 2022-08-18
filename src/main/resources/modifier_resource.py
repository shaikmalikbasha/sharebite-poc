import logging

from flask import request
from flask_restful import Resource
from src.main.models.modifier_model import Modifier
from src.main.models.section_model import ModifierSchema

modifier_schema = ModifierSchema()
modifiers_schema = ModifierSchema(many=True)


class ModifierResource(Resource):
    pass


class ModifierResourceList(Resource):
    def get(self):
        modifiers = Modifier.find_all()
        data = modifiers_schema.dump(modifiers)
        logging.info(data)
        return {"modifiers": data}

    def post(self):
        input_body = request.get_json()
        new_modifier = Modifier(description=input_body["description"])
        new_modifier.save()
        data = modifier_schema.dump(new_modifier)
        return {"created_modifer": data}, 201
