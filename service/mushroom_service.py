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

    def post_mushroom(self, mushroom_data, mushroom_image):
        # current_user = get_jwt_identity()
        try:
            if mushroom_image:  # Pastikan ada gambar yang diunggah
                # Simpan file gambar ke sistem penyimpanan (misalnya: direktori lokal)
                image_path = os.path.join('static', mushroom_image.filename)
                print(image_path)
                domain = "http://localhost:5000/"

                # Menggabungkan path dengan string domain
                
                mushroom_image.save(image_path)
                
                # Ubah path ke URL
                temp_path = url_for('static', filename=mushroom_image.filename)
                mushroom_data['path'] = urljoin(domain, temp_path)

            else:
                # Jika tidak ada gambar yang diunggah, hentikan program dan kembalikan respons yang sesuai
                abort(400, message="No image uploaded")
            new_mushroom = MushroomModel(**mushroom_data)
            db.session.add(new_mushroom)
            db.session.commit()

            return {"error": False, "message": "Mushroom added successfully"}
        except IntegrityError as e:
            # Jika user_id tidak valid
            abort(400, message="User id not valid"+ str(e))
        except SQLAlchemyError as e:
            # Kesalahan umum saat menyisipkan item
            print("SQLAlchemy Error:", str(e))  # Cetak detail kesalahan
            abort(500, message="An error occurred while inserting item: " + str(e))

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