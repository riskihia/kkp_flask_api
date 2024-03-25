from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import MushroomSchema, DetailMushroom
from util.example_response import GetAllMushroom, GetDetailMushroom
from service.mushroom_service import MushroomService

mushroom_blp = Blueprint(
    "Mushrooms", __name__, description="Option on Mushroom"
)


@mushroom_blp.route("/mushroom")
class Mushroom(MethodView):
    @mushroom_blp.doc(description="Get all mushrooms", tags=["Mushrooms"])
    @mushroom_blp.response(200, MushroomSchema(many=True), example=GetAllMushroom)
    def get(self):
        return MushroomService().get_all_mushroom()

@mushroom_blp.route("/mushroom/<string:name>")
class MushroomByName(MethodView):
    @mushroom_blp.doc(
        description="Get detail mushroom by name or id", tags=["Mushrooms"]
    )
    @mushroom_blp.response(200, DetailMushroom, example=GetDetailMushroom)
    @mushroom_blp.response(404, description="Mushroom not found")
    def get(self, name):
        return MushroomService().get_detail_mushroom_by_name_or_id(name)