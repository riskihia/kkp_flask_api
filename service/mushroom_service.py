import os
from urllib.parse import urljoin
from models import MushroomModel,EdibleModel, InedibleModel
from schemas import MushroomSchema, EdibleSchema, InedibleSchema
from util.config import db
from flask import jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_smorest import abort
from flask import request, url_for
from werkzeug.utils import secure_filename


class MushroomService:
    def __init__(self):
        pass

    def get_all_mushroom(self):
        try:
            mushroom = MushroomModel.query.filter(MushroomModel.deleted_at.is_(None)).all()

            mushroom_schema = MushroomSchema(many=True)

            response_data = {
                "error": False,
                "message": "Data mushroom fetched successfully",
                "data": mushroom_schema.dump(mushroom),
            }
            return jsonify(response_data), 200
        except Exception as e:
            print(e)
            
    def get_detail_mushroom_by_name_or_id(self, name):
        try:
            mushroom = MushroomModel.query.filter_by(name=name).first()
            mushroom_schema = MushroomSchema()

            if not mushroom:
                mushroom = MushroomModel.query.filter_by(id=name).first()
                if not mushroom:
                    response_data = {
                        "error": True,
                        "message": "Mushroom name is invalid"
                    }
                    return jsonify(response_data), 200

            # Fetch content based on mushroom type
            content = None
            if mushroom.type == 'edible':
                edible = EdibleModel.query.filter_by(mushroom_id=mushroom.id).first()
                if edible:
                    edible_schema = EdibleSchema()
                    content = edible_schema.dump(edible)
            elif mushroom.type == 'inedible':
                inedible = InedibleModel.query.filter_by(mushroom_id=mushroom.id).first()
                if inedible:
                    inedible_schema = InedibleSchema()
                    content = inedible_schema.dump(inedible)

            response_data = {
                "error": False,
                "message": "Data mushroom fetched successfully",
                "data": {
                    **mushroom_schema.dump(mushroom),
                    "content": content
                }
            }
            return jsonify(response_data), 200

        except Exception as e:
            print(e)
