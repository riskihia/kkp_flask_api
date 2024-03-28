from util.config import db
import datetime
import uuid, pytz
from datetime import datetime

from sqlalchemy import (
    Column,
    Double,
    ForeignKey,
    DateTime,
    Boolean,
    Integer,
    String,
    Text,
    Enum,
)

class TimeStamp:
    created_at = Column(DateTime, default=datetime.now(pytz.timezone("Asia/Jakarta")))
    updated_at = Column(
        DateTime,
        default=datetime.now(pytz.timezone("Asia/Jakarta")),
        onupdate=datetime.now(pytz.timezone("Asia/Jakarta")),
    )
    deleted_at = Column(DateTime, nullable=True)

class UserModel(db.Model, TimeStamp):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    token = Column(Text, nullable=True)

    users_mushrooms = db.relationship("UserMushroomModel", back_populates="user", lazy="dynamic", cascade="all, delete")

class UserMushroomModel(db.Model, TimeStamp):
    __tablename__ = "user_mushrooms"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    jenis_jamur = Column(String(250))
    path = Column(String(250), nullable=True)
    isEdible = Column(Boolean, nullable=True)
    description = Column(Text, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel", back_populates="users_mushrooms")

class MushroomModel(db.Model, TimeStamp):
    __tablename__ = "mushrooms"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    deskripsi = Column(Text, nullable=True)
    type = Column(String(250), nullable=False)

    edibles = db.relationship("EdibleModel", back_populates="mushroom", lazy="dynamic", cascade="all, delete")
    inedibles = db.relationship("InedibleModel", back_populates="mushroom", lazy="dynamic", cascade="all, delete")
    

class EdibleModel(db.Model, TimeStamp):
    __tablename__ = "edibles"

    id = Column(Integer, primary_key=True)
    kalori = Column(String(250), nullable=True)
    lemak = Column(String(250), nullable=True)
    protein = Column(String(250), nullable=True)
    karbohidrat = Column(String(250), nullable=True)
    mineral = Column(String(250), nullable=True)
    vitamin = Column(String(250), nullable=True)
    penggunaan_kuliner = Column(Text, nullable=True)
    manfaat_kesehatan = Column(Text, nullable=True)
    

    mushroom_id = Column(Integer, ForeignKey("mushrooms.id"), nullable=False)
    mushroom = db.relationship("MushroomModel", back_populates="edibles")

class InedibleModel(db.Model, TimeStamp):
    __tablename__ = "inedibles"
    id = Column(Integer, primary_key=True)
    toksisitas = Column(Text, nullable=True)
    gejala = Column(Text, nullable=True)

    mushroom_id = Column(Integer, ForeignKey("mushrooms.id"), nullable=False)
    mushroom = db.relationship("MushroomModel", back_populates="inedibles")