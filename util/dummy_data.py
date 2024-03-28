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
    if CekTabel("mushrooms") and not has_data(MushroomModel):
        insert_mushrooms()
    db.session.commit()

dataset = {
   "amanita_muscaria": {
      "type": "inedible",
      "deskripsi": "Amanita Muscaria adalah kelompok jamur beracun yang termasuk dalam genus Amanita. Mereka memiliki tudung merah dengan gumpalan bulu-bulu di pangkalan tudung.",
      "toksisitas": "Sangat beracun, mengandung muskimol dan ibotenic acid yang dapat merusak Sistem Saraf Pusat.",
      "gejala": "Gejalanya muncul dalam beberapa jam setelah konsumsi, seperti menyebabkan mual, muntah, kebingungan, seperti halusinasi, perubahan persepsi, dan gangguan koordinasi motorik."
   },

   "armillaria_borealis": {
      "type": "inedible",
      "deskripsi": "Armillaria Borealis dikenal sebagai jamur honey fungus, adalah spesies jamur yang umumnya ditemukan di hutan-hutan boreal di wilayah utara.",
      "toksisitas": "Beracun jika tidak diproses atau dimasak dengan baik.",
      "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, kebingungan, seperti halusinasi, perubahan persepsi."
   },

   "bjerkandera_adusta": {
      "type": "inedible",
      "deskripsi": "Bjerkandera adusta , juga dikenal sebagai smoky polypore, adalah jamur kayu yang umumnya ditemukan pada kayu yang membusuk, seperti batang pohon, cabang, dan tunggul.",
      "toksisitas": "Beracun, jika tidak diproses atau dimasak dengan baik.",
      "gejala": "Gejalanya mungkin tidak terlihat hingga 6-24 jam setelah konsumsi, tetapi dapat menyebabkan masalah pencernaan seperti mual, muntah, atau diare."
   },

   "chlorociboria_aeruginascens": {
      "type": "inedible",
      "deskripsi": "Chlorociboria aeruginascens adalah jamur cangkir biru-hijau yang indah. Jamur ini jarang memiliki tubuh buah yang terlihat, tetapi pewarnaan hijau yang dihasilkan oleh jamur ini pada kayu seringkali terlihat.",
      "toksisitas": "Sangat beracun, mengandung Xylindein yang dapat merusak hati dan ginjal.",
      "gejala": "Gejalanya mungkin tidak terlihat hingga 6-24 jam setelah konsumsi, tetapi dapat menyebabkan kegagalan organ dan kematian."
   },

   "daedaleopsis_tricolor": {
      "type": "inedible",
      "deskripsi": "Daedaleopsis tricolor adalah kelompok jamur beracun. Sering ditemukan pada kayu mati di hutan-hutan berdaun dan campuran. Jamur ini memiliki tudung yang berwarna coklat kemerahan hingga oranye dengan pola zonasi, dan porus berwarna putih hingga kekuningan di bagian bawah tudung.",
      "toksisitas": "Beracun jika dimakan mentah atau kurang dimasak.",
      "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, kebingungan, seperti halusinasi, perubahan persepsi."
   },

   "enoki": {
      "type": "Edible",
      "deskripsi": "Jamur Enoki memiliki tubuh buah yang panjang dan ramping dengan tutup yang kecil dan panjang. Biasanya berwarna putih, tetapi bisa menjadi coklat muda ketika terkena cahaya.",
      "nutrisi": {
         "kalori": "rendah",
         "vitamin": ["B", "D"],
         "mineral": ["zat besi", "kalsium", "potasium"]
      },
      "penggunaanKuliner": ["sup", "tumis", "salad"]
   },

   "ganoderma_applanatum": {
      "type": "Edible",
      "deskripsi": "Ganoderma applanatum, juga dikenal sebagai artist's bracket atau artist's conk, adalah jenis jamur yang sering ditemukan tumbuh di batang pohon mati atau terluka. Memiliki ciri khas berbentuk seperti papan atau kipas dengan permukaan atas yang keras dan berwarna cokelat hingga abu-abu.",
      "nutrisi": {
         "kalori": "rendah",
         "karbohidrat": "rendah",
         "protein": "tinggi",
         "lemak": "rendah",
         "vitamin": ["B2", "B1", "B6"],
         "mineral": ["zat besi", "kalsium", "Fosfor", "kalium"]
      },
      "manfaatKesehatan": [
         "Sebagai antioksidan untuk melawan radikal bebas",
         "Meningkatkan aktivitas sel kekebalan tubuh",
         "mengurangi peradangan dalam tubuh"
      ]
   },
     
   "gyromitra_infula": {
      "type": "inedible",
      "deskripsi": "Gyromitra Infula atau False Morel memiliki bentuk yang agak mirip dengan morel asli, tetapi berbeda dalam struktur dan kandungan kimia. Mereka sering ditemukan di hutan-hutan konifer dan daerah-daerah beriklim sedang.",
      "toksisitas": "Beracun, mengandung gyromitrin yang dapat merusak hati.",
      "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, dan kerusakan hati."
   },

   "kuping": {
      "type": "Edible",
      "deskripsi": "Jamur kuping memiliki bentuk yang menyerupai kuping manusia, dengan tudung yang tipis dan cembung. Mereka sering ditemukan tumbuh pada pohon-pohon yang telah mati di hutan-hutan.",
      "nutrisi": {
         "karbohidrat": "tinggi",
         "protein": "moderat",
         "vitamin": ["B", "C"],
         "mineral": ["zat besi", "kalsium"]
      },
      "penggunaanKuliner": [
         "dimasak dalam sup",
         "ditumis",
         "dimasak dalam masakan Tiongkok"
      ]
   },

   "leccinum_aurantiacum":{
      "type":"Edible",
      "deskripsi":"Leccinum aurantiacum adalah jamur konifer yang memiliki tudung berwarna oranye hingga cokelat tua dengan permukaan yang kasar.Jamur ini sering ditemukan di bawah pohon-pohon konifer di hutan-hutan beriklim sedang, terutama pada musim gugur dan musim semi.",
      "nutrisi":{
         "protein": "moderat",
         "vitamin": ["B", "D"],
         "mineral": ["zat besi", "kalium"]
      },
      "penggunaanKuliner": [
         "dimasak dalam sup",
         "ditumis",
         "ditambahkan ke pasta atau topping"
      ]
   },

   "pleurotus_pulmonarius": {
      "type": "Edible",
      "deskripsi": "Jamur Tiram Coklat, jamur ini umumnya dikenal sebagai jamur tiram India, jamur tiram Italia, jamur tiram coklat atau jamur tiram paru-paru",
      "nutrisi": {
         "protein": "tinggi",
         "vitamin": ["B", "D"],
         "mineral": ["zat besi", "kalsium", "Fosfor", "zink"]
      },
      "penggunaanKuliner": ["dipanggang", "ditumis", "dimasak dalam sup"]
   },
   
   "suillus_grevillei": {
      "type": "Edible",
      "deskripsi": "Suillus grevillei, memiliki tudung berbentuk cembung dengan permukaan yang licin dan berwarna cokelat keabu-abuan hingga kekuningan, sering dianggap sebagai jamur mikoriza yang membentuk hubungan simbiosis dengan pohon-pohon konifer.",
      "nutrisi": {
         "karbohidrat": "rendah",
         "protein": "tinggi",
         "vitamin": ["B", "D"],
         "mineral": ["zat besi", "selenium ", "kalium"]
      },
      "manfaatKesehatan": [
         "meningkatkan sistem kekebalan tubuh",
         "membantu kesehatan tulang",
         "mencegah masalah pencernaan seperti sembelit"
      ]
   },

   "tiram": {
      "type": "Edible",
      "deskripsi": "Tiram, juga dikenal sebagai jamur tiram, memiliki bentuk yang menyerupai kerang. Mereka memiliki tudung berwarna putih hingga abu-abu dengan pangkalan tudung yang lebar.",
      "nutrisi": {
         "protein": "tinggi",
         "vitamin": ["B", "D"],
         "mineral": ["zat besi", "kalsium", "zink"]
      },
      "penggunaanKuliner": ["dipanggang", "ditumis", "dimasak dalam sup"]
   },
   
   "trametes_hirsuta": {
    "type": "inedible",
    
    "deskripsi": "Trametes hirsute adalah kelompok jamur beracun. Dikenal karena permukaan berbulu yang dimilikinya. Jamur ini biasanya ditemukan tumbuh pada kayu mati atau membusuk di hutan-hutan.",
    "toksisitas": "Beracun jika dimakan mentah atau kurang dimasak.",
    "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, kebingungan, seperti halusinasi, perubahan persepsi."
 }
}



def edible_list():
    mushroom_list = [
        "enoki",
        "ganoderma_applanatum",
        "kuping",
        "leccinum_aurantiacum",
        "pleurotus_pulmonarius",
        "suillus_grevillei",
        "tiram"
    ]

    return mushroom_list

def inedible_list():
    mushroom_list = [
        "armillaria_borealis",
        "amanita_muscaria",
        "bjerkandera_adusta",
        "chlorociboria_aeruginascens",
        "daedaleopsis_tricolor",
        "gyromitra_infula",
        "trametes_hirsuta",
    ]

    return mushroom_list

def insert_mushrooms():
    for mushroom_name, mushroom_data in dataset.items():
        mushroom_model = MushroomModel(
            name=mushroom_name,
            deskripsi=mushroom_data.get('deskripsi'),
            type=mushroom_data.get('type')
        )
        db.session.add(mushroom_model)

        if mushroom_data['type'] == 'Edible':
            edible_data = mushroom_data.get('nutrisi', {})
            edible_model = EdibleModel(
                kalori=edible_data.get('kalori'),
                lemak=edible_data.get('lemak'),
                protein=edible_data.get('protein'),
                karbohidrat=edible_data.get('karbohidrat'),
                mineral=','.join(edible_data.get('mineral', [])),
                vitamin=','.join(edible_data.get('vitamin', [])),
                penggunaan_kuliner=','.join(mushroom_data.get('penggunaanKuliner', [])),
                manfaat_kesehatan=','.join(mushroom_data.get('manfaatKesehatan', [])),
                mushroom=mushroom_model
            )
            db.session.add(edible_model)
        else:
            inedible_model = InedibleModel(
                toksisitas=mushroom_data.get('toksisitas'),
                gejala=mushroom_data.get('gejala'),
                mushroom=mushroom_model
            )
            db.session.add(inedible_model)

    db.session.commit()

