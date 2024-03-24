from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)

from util.config import db

from models import UserModel
from schemas import UserSchema
from util.blocklist import BLOCKLIST


user_blp = Blueprint("Users", "users", description="Operations on users")


@user_blp.route("/register")
class UserRegister(MethodView):
    @user_blp.arguments(UserSchema)
    def post(self, store_data):
        username = store_data["username"]
        password = store_data["password"]

        # Cek apakah pengguna sudah ada di database
        user = (
            UserModel.query.filter(UserModel.username == store_data["username"])
            .first()
        )

        if user is None:
            # Buat pengguna baru dan simpan ke database
            new_user = UserModel(**store_data)
            db.session.add(new_user)
            db.session.commit()

            user = UserModel.query.filter(
                UserModel.username == store_data["username"]
            ).first()
            # Perbarui nilai store_data["token"] dengan token baru yang dibuat
            store_data["token"] = create_access_token(identity=user.username)
            new_token = store_data["token"]
            user.token = new_token
            db.session.commit()

            response = {
                "error": False,
                "message": "User successfully registered",
                "data": store_data,
            }
            return jsonify(response), 201
        
        abort(401, message="Username already exists.")


@user_blp.route("/login")
class UserLogin(MethodView):
    @user_blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")

@user_blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
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

    @user_blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200