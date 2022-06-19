import logging

from flask import request
from flask_restful import Resource
from src.main.models.item_model import Item


class ItemResource(Resource):
    pass


class ItemResourceList(Resource):
    def get(self):
        items = [item.to_dict() for item in Item.find_all()]
        logging.info(items)
        return {"items": items}

    def post(self):
        input_body = request.get_json()
        new_item = Item(**input_body)
        new_item.save()
        return {"created_section": new_item.to_json()}, 201
