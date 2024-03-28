import os

from flask_jwt_extended import get_jwt_identity, jwt_required
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import io
from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from keras.utils import load_img, img_to_array
import tensorflow as tf
from PIL import Image
import numpy as np 
import traceback
from util.example_response import PredictMushroom
from util.config import db
from models import MushroomModel, UserMushroomModel, EdibleModel, InedibleModel
from schemas import MushroomSchema, EdibleSchema, InedibleSchema 

predict_mushroom_blp = Blueprint(
    "Predict Mushrooms", __name__, description="Option on Predict Mushroom"
)


@predict_mushroom_blp.route("/predict-mushroom")
class Predict(MethodView):
    @jwt_required()
    @predict_mushroom_blp.response(200, example=PredictMushroom)
    def post(self):
        data = request.get_json()
        current_user = get_jwt_identity()

        user_mushroom = UserMushroomModel.query.filter_by(name=data["image_name"]).first()
        if not user_mushroom:
            response_data = {
                "error": True,
                "message": "Image name not found"
            }
            return jsonify(response_data), 404
        names = MushroomModel.query.with_entities(MushroomModel.name).all()
        categories = {str(i): name for i, (name,) in enumerate(names)}

        # Loading the model
        model_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'model.h5')
        model = tf.keras.models.load_model(model_path)
        try:
            # Constructing the absolute path to the image
            image_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'upload', data["image_name"])

            # Opening the image
            with open(image_path, 'rb') as image_file:
                image = Image.open(io.BytesIO(image_file.read()))
                image = image.resize((256, 256))
                # Convert image to RGB mode
                image = image.convert("RGB")

            image_array = img_to_array(image)
            image_expanded = np.expand_dims(image_array, axis=0)
            image_expanded /= 255.0

            result = model.predict(image_expanded)
            predicted_category_index = np.argmax(result)
            predicted_category_name = categories[str(predicted_category_index)]

             # Update UserMushroomModel
            user_mushroom = UserMushroomModel.query.filter_by(user_id=current_user, name=data["image_name"]).first()
            if user_mushroom:
                user_mushroom.jenis_jamur = predicted_category_name
                db.session.commit()

            # Update MushroomModel
            mushroom = MushroomModel.query.filter_by(name=predicted_category_name).first()
            content = None
            mushroom_schema = MushroomSchema()
            
            if mushroom:
                user_mushroom.isEdible = (mushroom.type.lower() == 'edible')
                user_mushroom.description = mushroom.deskripsi
                db.session.commit()

            if mushroom.type.lower() == 'edible':
                edible = EdibleModel.query.filter_by(mushroom_id = mushroom.id).first()
                edible_schema = EdibleSchema()  #  karena Anda mengambil semua entri
                # response_data = {
                #     "error": False,
                #     "message": "Hasil scan image " + data["image_name"],
                #     "data": edible_schema.dump(edibles),  # serialize data dengan schema
                # }
                # return jsonify(response_data), 200
                content = edible_schema.dump(edible)
                
            else:
                inedible = InedibleModel.query.filter_by(mushroom_id = mushroom.id).first()
                inedible_schema = InedibleSchema()  #  karena Anda mengambil semua entri
                # response_data = {
                #     "error": False,
                #     "message": "Hasil scan image " + data["image_name"],
                #     "data": inedible_schema.dump(inedibles),  # serialize data dengan schema
                # }
                # return jsonify(response_data), 200
                content = inedible_schema.dump(inedible)
        
            response_data = {
                "error": False,
                "message": "Data mushroom predicted successfully",
                "data": {
                    **mushroom_schema.dump(mushroom),
                    "content": content
                }
            }
            return jsonify(response_data), 200
        except Exception as e:
            return {
                "result": "Image not found",
                "error": f"Internal Server Error: {str(e)}"
            }

