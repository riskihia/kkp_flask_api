import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import io
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from keras.utils import load_img, img_to_array
import tensorflow as tf
from PIL import Image
import numpy as np 
import traceback

predict_mushroom_blp = Blueprint(
    "Predict Mushrooms", __name__, description="Option on Predict Mushroom"
)


@predict_mushroom_blp.route("/predict-mushroom")
class Predict(MethodView):
    def get(self):
        categories = {
            0: "amanita_muscaria",
            1: "armillaria_borealis",
            2: "bjerkandera_adusta",
            3: "chlorociboria_aeruginascens",
            4: "daedaleopsis_tricolor",
            5: "enoki",
            6: "ganoderma_applanatum",
            7: "gyromitra_infula",
            8: "kuping",
            9: "leccinum_aurantiacum",
            10: "pleurotus_pulmonarius",
            11: "suillus_grevillei",
            12: "tiram",
            13: "trametes_hirsuta"
        }
        # Loading the model
        model_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'model.h5')
        model = tf.keras.models.load_model(model_path)
        try:
            # Constructing the absolute path to the image
            image_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'upload', 'jamur2.jpg')

            # Opening the image
            with open(image_path, 'rb') as image_file:
                image = Image.open(io.BytesIO(image_file.read()))
                image = image.resize((256, 256))
                # Convert image to RGB mode
                image = image.convert("RGB")


            # image = image.resize((256, 256))
            # img = cv2.resize(img,(224,224)) 
            # image = image.reshape(None, 256, 256, 3) 
            image_array = img_to_array(image)
            image_expanded = np.expand_dims(image_array, axis=0)
            image_expanded /= 255.0

            result = model.predict(image_expanded)
            return {"result": categories[np.argmax(result)]}
            # Convert result to JSON and return
            # result_json = jsonify(result.tolist())
            # return result_json
        except Exception as e:
            traceback.print_exc()
            return f"Internal Server Error: {str(e)}"
