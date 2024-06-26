from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from service.user_service import UserService
from util.example_response import RegisterSuccess, LoginSuccess
from util.config import db
from schemas import UserSchema

from models import UserModel
from schemas import UserSchema
from util.blocklist import BLOCKLIST


user_blp = Blueprint("Users", "users", description="Operations on users")


@user_blp.route("/register")
class UserRegister(MethodView):
    @user_blp.arguments(UserSchema)
    @user_blp.response(200, example=RegisterSuccess)
    @user_blp.response(422, example=None)
    def post(self, store_data):
        # return store_data
        return UserService.register(store_data)


@user_blp.route("/login")
class UserLogin(MethodView):
    @user_blp.arguments(UserSchema)
    @user_blp.response(200, example=LoginSuccess)
    @user_blp.response(422, example=None)
    def post(self, user_data):
        return UserService.login(user_data)
        

@user_blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    @user_blp.response(200, example=LoginSuccess)
    @user_blp.response(422, example=None)
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200

@user_blp.route("/user/<int:user_id>")
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful
    when we are manipulating data regarding the users.
    """

    @jwt_required()
    def get(self, user_id):
        user_schema = UserSchema()
        user = UserModel.query.get_or_404(user_id)
        response_data = {
            "error": False,
            "message": "Data user fetched successfully",
            "data": user_schema.dump(user),
        }
        return jsonify(response_data), 200

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200