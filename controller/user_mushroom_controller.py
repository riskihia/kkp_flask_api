from flask.views import MethodView
from flask import request
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from schemas import MushroomSchema, UserMushroomSchema
from util.example_response import GetAllMushroom, PostMushroom
from service.user_mushroom_service import UserMushroomService
# from flask_jwt_extended import jwt_required

user_mushroom_blp = Blueprint(
    "User Mushrooms", __name__, description="Option on User Mushroom"
)


@user_mushroom_blp.route("/user-mushroom")
class Mushroom(MethodView):
    # @jwt_required()
    @user_mushroom_blp.response(200, example=GetAllMushroom)
    def get(self):
        return UserMushroomService().get_all_mushroom()

    @jwt_required()
    @user_mushroom_blp.arguments(UserMushroomSchema, location='form')
    @user_mushroom_blp.response(200, example=PostMushroom)
    @user_mushroom_blp.response(422, example=None)
    def post(self, mushroom_data):
        mushroom_data = dict(request.form)
        mushroom_image = request.files.get('image')  # Ambil file gambar dari permintaan
        return UserMushroomService().post_mushroom(mushroom_data, mushroom_image)
    

