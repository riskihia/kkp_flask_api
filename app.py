from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from datetime import datetime
from controller import *
import pytz, os
from util.config import db, Config
from util import jwt_config
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

    blueprints = [
        user_controller.user_blp,
        mushroom_controller.mushroom_blp,
    ]

    for bp in blueprints:
        api.register_blueprint(bp)

    return app

app = create_app()