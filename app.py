from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from datetime import datetime
from controller import *
import pytz, os
from util.config import db, Config
from util import jwt_config
from util.dummy_data import insert_mushrooms
from schemas import UserSchema, MushroomSchema

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.before_request
    def set_timezone():
        timezone = pytz.timezone("Asia/Jakarta")
        datetime.now(timezone)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt_config.init_app(app)
    api = Api(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()
        # insert_mushrooms()

    blueprints = [
        user_controller.user_blp,
        user_mushroom_controller.user_mushroom_blp,
        mushroom_controller.mushroom_blp,
    ]

    for bp in blueprints:
        api.register_blueprint(bp)

    return app

app = create_app()