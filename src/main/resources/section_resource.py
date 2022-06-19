import logging

from flask import request
from flask_restful import Resource
from src.main.models.section_model import Section


class SectionResource(Resource):
    pass


class SectionResourceList(Resource):
    def get(self):
        sections_result_set = Section.find_all()
        sections = [section.to_dict() for section in sections_result_set]
        logging.info(sections)
        return {"sections": sections}, 200

    def post(self):
        input_body = request.get_json()
        new_section = Section(**input_body)
        new_section.save()
        return {"created_section": new_section.to_json()}, 201
