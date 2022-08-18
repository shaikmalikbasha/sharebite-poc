import logging

from flask import request
from flask_restful import Resource
from src.main.models.item_model import Item
from src.main.models.section_model import ItemSchema

items_schema = ItemSchema(many=True)
item_schema = ItemSchema()


class ItemResource(Resource):
    pass


class ItemResourceList(Resource):
    def get(self):
        items_result_set = Item.find_all()
        data = items_schema.dump(items_result_set)
        logging.info(data)
        return {"items": data}

    def post(self):
        input_body = request.get_json()
        new_item = Item(**input_body)
        new_item.save()
        return {"created_section": new_item.to_json()}, 201
