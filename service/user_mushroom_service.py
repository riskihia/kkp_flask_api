import os
import random
import string
from urllib.parse import urljoin

from flask_jwt_extended import get_jwt_identity
from sqlalchemy import desc
from models import UserMushroomModel
from schemas import GetUserMushroomSchema, UserMushroomSchema , DetailUserMushroomSchema
from util.config import db
from flask import jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_smorest import abort
from flask import request, url_for
from werkzeug.utils import secure_filename


class UserMushroomService:
    def __init__(self):
        pass

    def post_mushroom(self, mushroom_data, mushroom_image):
        current_user = get_jwt_identity()
        
        try:
            if mushroom_image: 
                # Generate random string for unique identifier
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

                # Extract original filename and extension
                file_extension = os.path.splitext(mushroom_image.filename)[1]
                image_name = mushroom_data['name'].replace(' ', '_')
                new_filename = f"{image_name}_{random_string}{file_extension}"
                # return "selesai"

                # Specify upload directory
                upload_folder = os.path.join('static', 'upload')

                # Create upload directory if it doesn't exist
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                # Save the image to the upload directory with the new filename
                image_path = os.path.join(upload_folder, new_filename)
                mushroom_image.save(image_path)

                # Generate URL for the uploaded image
                domain = "http://localhost:5000/"
                temp_path = os.path.join('static/upload/', new_filename)
                mushroom_data['path'] = urljoin(domain, temp_path)
                mushroom_data['name'] = new_filename

            else:
                # Jika tidak ada gambar yang diunggah, hentikan program dan kembalikan respons yang sesuai
                abort(400, message="No image uploaded")

            # Create a new instance of MushroomModel with mushroom_data
            new_mushroom = UserMushroomModel(**mushroom_data)

            # Add user_id to the new_mushroom
            new_mushroom.user_id = current_user

            # Add the new_mushroom to the session and commit
            db.session.add(new_mushroom)
            db.session.commit()

            response_data = {
                "error": False,
                "message": "Data mushroom added successfully",
            }
            return jsonify(response_data), 200
        except IntegrityError as e:
            # Jika user_id tidak valid
            abort(400, message="User id not valid"+ str(e))
        except SQLAlchemyError as e:
            # Kesalahan umum saat menyisipkan item
            print("SQLAlchemy Error:", str(e))  # Cetak detail kesalahan
            abort(500, message="An error occurred while inserting item: " + str(e))


    def find_mushroom(self, name):
        current_user = get_jwt_identity()
        try:
            detail_user_mushroom_schema = DetailUserMushroomSchema()
            mushrooms = UserMushroomModel.query.filter(
                UserMushroomModel.name.like(f'%{name}%'), 
                UserMushroomModel.user_id == current_user
                ).first()
            if mushrooms:
                response_data = {
                    "error": False,
                    "message": "Data mushroom fetched successfully",
                    "data": detail_user_mushroom_schema.dump(mushrooms),
                }
                return jsonify(response_data), 200
            else:
                # Proses jika jamur tidak ditemukan
                return jsonify({"message": "No mushrooms found with that name for the current user"}), 404
        except Exception as e:
            print(e)

    def get_all_mushroom(self):
        current_user = get_jwt_identity()
        try:
            mushrooms = UserMushroomModel.query.filter(UserMushroomModel.deleted_at.is_(None),UserMushroomModel.user_id == current_user).order_by(desc(UserMushroomModel.created_at)).all()

            mushroom_schema = GetUserMushroomSchema(many=True)

            response_data = {
                "error": False,
                "message": "Data mushroom fetched successfully",
                "data": mushroom_schema.dump(mushrooms),
            }
            return jsonify(response_data), 200
        except Exception as e:
            print(e)