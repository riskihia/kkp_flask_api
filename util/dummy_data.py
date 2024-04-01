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

   "amanita_rubescens": {
      "type": "inedible",
      "deskripsi": "Armillaria Borealis dikenal sebagai jamur honey fungus, adalah spesies jamur yang umumnya ditemukan di hutan-hutan boreal di wilayah utara.",
      "toksisitas": "Beracun jika tidak diproses atau dimasak dengan baik.",
      "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, kebingungan, seperti halusinasi, perubahan persepsi."
   },

   "Boletus Edulis": {
      "type": "Edible",
      "deskripsi": "Boletus edulis atau jamur babi bayi (bahasa Inggris: penny bun, cep, porcino atau porcini) tersebar luas di belahan bumi utara di Eropa, Asia, dan Amerika Utara. Jamur ini tumbuh di hutan peluruh dan konifer dan perkebunan. Jamur ini salah satu jamur yang paling banyak dicari dan dikonsumsi di dunia. Jamur ini terkenal karena rasanya yang lezat dan teksturnya yang unik.",
      "nutrisi": {
         "protein": "tinggi",
         "vitamin": ["B"],
         "mineral": ["kalium", "Fosfor", "selenium "]
      },
      "penggunaanKuliner": [
         "dimasak dalam sup", 
         "sebagai campuran pasta atau risotto"
      ]
   },

   "Calycina citrina": {
      "type": "inedible",
      "deskripsi": "Calycina citrina, umumnya dikenal sebagai cangkir peri kuning, adalah spesies fungi yang berasal dari keluarga Helotiaceae. Jamur ini berbentuk cangkir kecil berwarna kuning dengan diameter 3 mm, dan seringkali tidak memiliki tangkai, tubuh buahnya biasa berkelompok di atas kayu lapuk. Spesies ini umumnya ditemukan di Afrika Utara, Asia, Eropa, Amerika Utara, Amerika Tengah, dan Amerika Selatan.",
      "toksisitas": "tidak beracun, namun tetap diperlukan kehati-hatian dalam identifikasi yang akurat serta disarankan untuk menghindari mengkonsumsi jamur ini.",
      "gejala": "ruam kulit, gatal-gatal, atau masalah pencernaan."
   },

   "Cerioporus squamosus": {
      "type": "Edible",
      "deskripsi": "Cerioporus_squamosus atau Dryad’s saddle atau pelana Driad tergabung dalam famili Polyporaceae dan genus Cerioporus, cukup populer dengan julukan jamur punggung burung. Umumnya dimanfaatkan sebagai bahan pangan dan telah dibudidayakan di beberapa negara. Di alam, jamur ini umumnya tumbuh di kayu baik pada hutan ataupun daerah yang dekat dengan kegiatan manusia. ",
      "nutrisi": {
         "protein": "tinggi",
         "karbohidrat": "tinggi",
         "vitamin": ["B", "D"],
         "mineral": ["kalsium", "kalium", "Fosfor", "natrium"]
      },
      "penggunaanKuliner": [
         "ditumis", 
         "dimasak dalam sup",
         "dipanggang"
      ]
   },

   "Flammulina velutipes": {
      "type": "Edible",
      "deskripsi": "Flammulina velutipes atau jamur Enoki memiliki tubuh buah yang panjang dan ramping dengan tutup yang kecil dan panjang. Biasanya berwarna putih, tetapi bisa menjadi coklat muda ketika terkena cahaya.",
      "nutrisi": {
         "kalori": "rendah",
         "vitamin": ["B", "D"],
         "mineral": ["zat besi", "kalsium", "potasium"]
      },
      "penggunaanKuliner": [
         "dimasak dalam sup", 
         "ditumis", 
         "dipanggang", 
         "salad"
      ]
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
     
   "Fomes fomentarius": {
      "type": "inedible",
      "deskripsi": "Fomes fomentarius atau tirhau selampahan adalah spesies patogen tanaman jamur yang ditemukan di Eropa, Asia, Afrika, dan Amerika Utara. Jamur yang bentuknya mirip tapak kuda sering dimanfaatkan untuk membuat bahan kulit. Menurut penelitian jamur ini berpotensi besar diaplikasikan dalam produksi bahan multifungsi di masa depan. ",
      "toksisitas": "tidak beracun, namun tetap diperlukan kehati-hatian dalam identifikasi yang akurat serta disarankan untuk menghindari mengkonsumsi jamur ini.",
      "gejala": "penggunaan jamur ini dalam dosis tinggi atau dalam jangka waktu yang panjang dapat menyebabkan beberapa efek samping seperti gangguan pencernaan, reaksi alergi, interaksi obat, dan potensi risiko keracunan jika tidak disiapkan dengan benar."
   },

   "Gyromitra Gigas": {
      "type": "inedible",
      "deskripsi": "Gyromitra Gigas atau False Morel memiliki bentuk yang agak mirip dengan morel asli, tetapi berbeda dalam struktur dan kandungan kimia. Mereka sering ditemukan di hutan-hutan konifer dan daerah-daerah beriklim sedang.",
      "toksisitas": "Sangat beracun, mengandung gyromitrin yang dapat merusak hati.",
      "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, dan kerusakan hati."
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

   "Paxillus involutus": {
      "type": "inedible",
      "deskripsi": "Paxillus involutus (atau Brown Roll-rim atau Poison Pax) adalah spesies jamur ektomikoriza yang tersebar luas, ditemukan di bawah beragam pohon, dan membentuk hubungan erat dengan akar pohon dari berbagai spesies. ",
      "toksisitas": "Beracun, mengandung senyawa glikoprotein berbahaya bagi tubuh. ",
      "gejala": "menyebabkan Autoimmune hemolytic anemia yang muncul beberapa tahun kemudian setelah menkonsumsi jamur,menyebabkan hemolisis yang parah, gagal ginjal, dan bahkan hingga menyebabkan kematian."
   },
   
   "Pleurotus ostreatus": {
      "type": "Edible",
      "deskripsi": "Pleurotus ostreatus atau jamur tiram sering dikenal dengan sebutan King Oyster Mushroom, adalah jamur pangan dari kelompok Basidiomycota dan termasuk kelas Homobasidiomycetes dengan ciri-ciri umum tubuh buah berwarna putih hingga krem dan tudungnya berbentuk setengah lingkaran mirip cangkang tiram dengan bagian tengah agak cekung. ",
      "nutrisi": {
         "protein": "tinggi",
         "karbohidrat": "rendah",
         "vitamin": ["B", "C" ,"D"],
         "mineral": ["zat besi", "kalsium", "Fosfor", "zink"]
      },
      "penggunaanKuliner": ["dipanggang", "ditumis", "dimasak dalam sup"]
   },

   "Schizophyllum commune": {
      "type": "inedible",
      "deskripsi": "Schizophyllum commune atau jamur gerigit adalah spesies jamur dalam genus Schizophyllum . Jamur ini menyerupai kipas gelombang dari terumbu karang yang padat. Ia memiliki gerigit yang bentuknya bervariasi dari kuning krem hingga putih pucat.",
      "toksisitas": "Beracun jika dimakan mentah atau kurang dimasak.",
      "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk mual, muntah, diare, kebingungan, seperti halusinasi, perubahan persepsi."
   },
   
   "Trichaptum biforme": {
    "type": "inedible",
    "deskripsi": "Jamur Violet-toothed Polypore (Trichaptum biforme) adalah jamur yang sangat umum di Amerika Utara yang tidak bisa dimakan atau dimanfaatkan secara medis, tetapi seringkali disalahartikan dengan jamur Turkey Tail (Trametes versicolor) yang memiliki manfaat medis yang kuat. Namun, perhatikan bagian bawahnya! Bagian bawah dari Violet-toothed Polypore memiliki gigi-gigi kecil dan sering berwarna ungu, memudar menjadi cokelat atau ungu saat penuaan.",
    "toksisitas": "Beracun. ",
    "gejala": "Gejalanya mungkin muncul setelah beberapa jam hingga beberapa hari setelah konsumsi, termasuk gangguan pencernaan seperti mual, muntah, dan diare, serta reaksi alergi seperti ruam kulit atau sesak napas pada beberapa individu. Meskipun jarang terjadi, keracunan juga mungkin terjadi dengan gejala seperti pusing, sakit kepala, atau masalah pernapasan."
 }
}



def edible_list():
    mushroom_list = [
        "Boletus Edulis",
        "Cerioporus squamosus",
        "Flammulina velutipes",
        "ganoderma_applanatum",
        "leccinum_aurantiacum",
        "Pleurotus ostreatus",
    ]

    return mushroom_list

def inedible_list():
    mushroom_list = [
        "armillaria_borealis",
        "amanita_muscaria",
        "Calycina citrina",
        "Fomes fomentarius",
        "Gyromitra Gigas",
        "Paxillus involutus",
        "Schizophyllum commune",
        "Trichaptum biforme",
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

