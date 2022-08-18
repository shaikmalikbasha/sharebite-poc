import logging

from flask import request
from flask_restful import Resource
from src.main.models.section_model import Section, SectionSchema

section_schema_obj = SectionSchema()
sections_schema_obj = SectionSchema(many=True)


class SectionResource(Resource):
    pass


class SectionResourceList(Resource):
    def get(self):
        sections_result_set = Section.find_all()
        data = sections_schema_obj.dump(sections_result_set)
        logging.info(data)
        return {"sections": data}, 200

    def post(self):
        input_body = request.get_json()
        new_section = Section(**input_body)
        new_section.save()
        return {"created_section": new_section.to_json()}, 201
