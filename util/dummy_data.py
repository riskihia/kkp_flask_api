import datetime
import uuid
from util.config import db
from models import MushroomModel, EdibleModel, InedibleModel
from sqlalchemy import inspect
import random


def has_data(model):
    count = db.session.query(db.func.count()).select_from(model).scalar()
    return count > 0


def CekTabel(nama_table):
    inspector = inspect(db.engine)
    return inspector.has_table(nama_table)


def populate_data():
    # if CekTabel("mushrooms") and not has_data(MushroomModel):
    #     insert_mushrooms()
    # if CekTabel("edibles") and not has_data(EdibleModel):
    #     insert_edible()
    # if CekTabel("inedibles") and not has_data(InedibleModel):
    #     insert_inedibles()

    db.session.commit()

def edible_list():
    mushroom_list = [
        "Champignon",
        "Maitake",
        "Tiram",
        "enoki",
        "kuping",
        "shitake",
        "truffle"
    ]

    return mushroom_list

def inedible_list():
    mushroom_list = [
        "Autumn Skullcap",
        "Death Cap",
        "Destroying Angels",
        "False Morel",
        "Poison Fire Coral"
    ]

    return mushroom_list

def insert_mushrooms():
    edible = edible_list()
    inedible = inedible_list()
    for item in edible:
        mushroom_edible = MushroomModel(
            name = item,
            type = "edible"
        )
        db.session.add(mushroom_edible)
    
    for item in inedible:
        mushroom_inedible = MushroomModel(
            name = item,
            type = "inedible"
        )
        db.session.add(mushroom_inedible)

def insert_edible():
    edible_mushrooms = MushroomModel.query.filter_by(type='edible').all()

def generate_dummy_data():
    edible_mushrooms = edible_list()
    inedible_mushrooms = inedible_list()

    edible_data = []
    inedible_data = []

    # Generate dummy data for edible mushrooms
    for name in edible_mushrooms:
        mushroom_data = {
            "name": name,
            "type": "edible",
            "content": {
                "kalori": str(random.randint(5, 20)),  # Generate random values for demonstration
                "lemak": str(random.randint(20, 40)),
                "natrium": str(random.randint(30, 50)),
                "kalium": str(random.randint(1, 10)),
                "karbohidrat": str(random.randint(1, 10)),
            }
        }
        edible_data.append(mushroom_data)

    # Generate dummy data for inedible mushrooms
    for name in inedible_mushrooms:
        mushroom_data = {
            "name": name,
            "type": "inedible",
            "content": {
                "poison": str(random.randint(50, 100)),  # Generate random values for demonstration
            }
        }
        inedible_data.append(mushroom_data)

    # Combine both lists
    dataset = edible_data + inedible_data

    return dataset

# Example usage
dummy_data = generate_dummy_data()
print(dummy_data)