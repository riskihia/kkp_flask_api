import os
from urllib.parse import urljoin
from models import UserModel
from schemas import MushroomSchema
from util.config import db
from flask import jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_smorest import abort
from flask import request, url_for
from werkzeug.utils import secure_filename
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from passlib.hash import pbkdf2_sha256


class UserService:
    def __init__(self):
        pass

    def register(store_data):
        try:
            # Cek apakah pengguna sudah ada di database
            user = (
                UserModel.query.filter(UserModel.username == store_data["username"])
                .first()
            )

            if user is None:
                # Hash password sebelum menyimpannya
                hashed_password = pbkdf2_sha256.hash(store_data["password"])
                
                # Update store_data dengan password yang di-hash
                store_data["password"] = hashed_password
                # Buat pengguna baru dan simpan ke database
                new_user = UserModel(**store_data)
                db.session.add(new_user)
                db.session.commit()

                response = {
                    "error": False,
                    "message": "User successfully registered",
                }
                return jsonify(response), 201
            
            response = {
                    "error": False,
                    "message": "Username or Password is invalid",
                }
            return jsonify(response), 404
        except Exception as e:
            print(e)
    
    def login(store_data):
        try:
            user = UserModel.query.filter(
                UserModel.username == store_data["username"]
            ).first()
            
            if user and pbkdf2_sha256.verify(store_data["password"], user.password):
                access_token = create_access_token(identity=user.id)
                user.token = access_token
                db.session.commit() 
                response = {
                    "error": False,
                    "message": "Login Successfully",
                    "access_token" : access_token
                }
                print("cek cek")
                return jsonify(response), 200
            response = {
                "error": True,
                "message": "Username or Password is invalid",
            }
            return jsonify(response), 404
        except Exception as e:
            print(str(e))
            response = {
                "error": True,
                "message": "An error occurred while processing your request."
            }
            return jsonify(response), 500