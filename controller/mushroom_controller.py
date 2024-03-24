from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint
from schemas import MushroomSchema
from util.example_response import GetAllMushroom, PostMushroom
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
    @mushroom_blp.response(200, example=GetAllMushroom)
    def get(self):
        return MushroomService().get_all_mushroom()

    # @jwt_required()
    @mushroom_blp.arguments(MushroomSchema)
    @mushroom_blp.response(200, example=PostMushroom)
    @mushroom_blp.response(422, example=None)
    def post(self, mushroom_data):
        mushroom_data = dict(request.form)
        mushroom_image = request.files.get('image')  # Ambil file gambar dari permintaan
        return MushroomService().post_mushroom(mushroom_data, mushroom_image)