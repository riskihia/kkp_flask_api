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
        poison_names = ["Cyanide", "Amanitin", "Orellanine", "Gyromitrin", "Tetrodotoxin"]
        poison_name = random.choice(poison_names)
        mushroom_data = {
            "name": name,
            "type": "inedible",
            "content": {
                "poison_name": poison_name,
                "amount": str(random.randint(50, 100))  # Generate random values for demonstration
            }
        }
        inedible_data.append(mushroom_data)

    # Combine both lists
    dataset = edible_data + inedible_data

    return dataset

def insert_mushrooms():
    dataset = generate_dummy_data()
    
    for item in dataset:
        mushroom = MushroomModel(
            name=item['name'],
            type=item['type']
        )
        db.session.add(mushroom)

        if item['type'] == 'edible':
            edible = EdibleModel(
                kalori=item['content']['kalori'],
                lemak=item['content']['lemak'],
                natrium=item['content']['natrium'],
                kalium=item['content']['kalium'],
                karbohidrat=item['content']['karbohidrat'],
                mushroom=mushroom
            )
            db.session.add(edible)
        elif item['type'] == 'inedible':
            inedible = InedibleModel(
                poison_name=item['content']['poison_name'],
                amount=item['content']['amount'],
                mushroom=mushroom
            )
            db.session.add(inedible)

    db.session.commit()

# def insert_mushrooms():
#     dataset = generate_dummy_data()
    
#     for item in dataset:
#         mushroom_edible = MushroomModel(
#             name = item['name'],
#             type = item["type"]
#         )
#         db.session.add(mushroom_edible)
    
#     db.session.commit()