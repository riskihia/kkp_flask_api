from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import MushroomSchema
from util.example_response import GetAllMushroom, PostMushroom
from service.mushroom_service import MushroomService

mushroom_blp = Blueprint(
    "mushroom", __name__, description="Option in Mushroom"
)


@mushroom_blp.route("/mushroom")
class Mushroom(MethodView):
    @mushroom_blp.doc(description="Get all mushrooms", tags=["Mushroom"])
    @mushroom_blp.response(200, example=GetAllMushroom)
    def get(self):
        return MushroomService().get_all_mushroom()

@mushroom_blp.route("/mushroom/<string:name>")
class MushroomByName(MethodView):
    @mushroom_blp.doc(
        description="Get mushroom by name", tags=["Mushroom"], params={"name": "Mushroom name"}
    )
    @mushroom_blp.response(200, MushroomSchema)
    @mushroom_blp.response(404, description="Mushroom not found")
    def get(self, name):
        return MushroomService().get_mushroom_by_name(name)