import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import io
from flask.views import MethodView
from flask_smorest import Blueprint
from keras.utils import load_img, img_to_array
import tensorflow as tf
from PIL import Image

predict_mushroom_blp = Blueprint(
    "Predict Mushrooms", __name__, description="Option on Predict Mushroom"
)


@predict_mushroom_blp.route("/predict-mushroom")
class Predict(MethodView):
    def get(self):
        model_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'model.h5')
        model = tf.keras.models.load_model(model_path)

        image = Image.open(io.BytesIO(image_data))
        return model_path
