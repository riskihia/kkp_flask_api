from models import MushroomModel
from schemas import MushroomSchema
from util.config import db
from flask import jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_smorest import abort

class MushroomService:
    def __init__(self):
        pass

    def post_mushroom(self, mushroom_data):
        # current_user = get_jwt_identity()
        try:
            # mushroom_data["id"] = str(uuid.uuid4())
            # lahan_data["user_id"] = current_user
            # random_photo = random.choice([l.photo for l in lahan])
            # lahan_data["photo"] = random_photo

            new_mushroom = MushroomModel(**mushroom_data)
            db.session.add(new_mushroom)
            db.session.commit()

            return {"error": False, "message": "Mushroom added successfully"}
        except IntegrityError:
            # Jika user_id tidak valid
            abort(400, message="User id not valid")
        except SQLAlchemyError:
            # Kesalahan umum saat menyisipkan item
            abort(500, message="An error occurred while inserting item")

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