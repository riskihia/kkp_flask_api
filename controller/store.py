import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import StoreSchema


from util.config import db

from models import StoreModel

store_blp = Blueprint("Stores", __name__, description="Operations on stores")


@store_blp.route("/store/<string:store_id>")
class Store(MethodView):
    @store_blp.response(200, StoreSchema)
    def get(cls, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(cls, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}, 200


@store_blp.route("/store")
class StoreList(MethodView):
    @store_blp.response(200, StoreSchema(many=True))
    def get(cls):
        return StoreModel.query.all()

    @store_blp.arguments(StoreSchema)
    @store_blp.response(201, StoreSchema)
    def post(cls, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")

        return store