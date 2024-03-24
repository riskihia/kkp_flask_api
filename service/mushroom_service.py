import os
from urllib.parse import urljoin
from models import MushroomModel
from schemas import MushroomSchema
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

    def get_mushroom_by_name(self, name):
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
                    

            response_data = {
                "error": False,
                "message": "Data mushroom fetched successfully",
                "data": mushroom_schema.dump(mushroom),
            }
            return jsonify(response_data), 200
            
        except Exception as e:
            print(e)