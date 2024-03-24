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
    password = Column(String(80), nullable=False)
    token = Column(Text, nullable=True)

class MushroomModel(db.Model, TimeStamp):
    __tablename__ = "mushrooms"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    type = Column(String(80), nullable=False)
    path = Column(String(80), nullable=False)
    ext = Column(String(80), nullable=True)
    contents = db.relationship("ContentModel", back_populates="mushroom", lazy="dynamic")

class ContentModel(db.Model, TimeStamp):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True)
    kalori = Column(Double, nullable=True)
    lemak = Column(Double, nullable=True)
    natrium = Column(Double, nullable=True)
    kalium = Column(Double, nullable=True)
    Karbohidrat = Column(Double, nullable=True)

    mushroom_id = Column(Integer, ForeignKey("mushrooms.id"), nullable=False)

    mushroom = db.relationship("MushroomModel", back_populates="contents")