from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from datetime import datetime
from controller import *
import pytz, os
from util.config import db, Config
from util import jwt_config

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

    # with app.app_context():
    #     db.create_all()
        # populate_data()

    blueprints = [
        item.item_blp,
        store.store_blp,
        tag.tag_blp,
        user.user_blp,
    ]

    for bp in blueprints:
        api.register_blueprint(bp)

    return app

app = create_app()