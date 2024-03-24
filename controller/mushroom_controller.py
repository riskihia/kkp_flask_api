from flask.views import MethodView
from flask_smorest import Blueprint
from models import MushroomModel
from schemas import MushroomSchema
from flask import jsonify, request
# from util.example_response import (
#     GetLahanExample,
#     PostLahanExample,
#     DeleteLahanExample,
#     GetLahanIdExample,
# )
from service.mushroom_service import MushroomService
# from flask_jwt_extended import jwt_required

mushroom_blp = Blueprint(
    "mushroom", __name__, description="Option in Mushroom"
)


@mushroom_blp.route("/mushroom")
class Mushroom(MethodView):
    # @jwt_required()
    @mushroom_blp.response(200, MushroomSchema(many=True))
    # @mushroom_blp.response(200, example=GetLahanExample)
    def get(self):
        return MushroomService().get_all_mushroom()

    # @jwt_required()
    @mushroom_blp.arguments(MushroomSchema)
    # @mushroom_blp.response(201, example=PostLahanExample)
    def post(self, mushroom_data):
        return MushroomService().post_mushroom(mushroom_data)