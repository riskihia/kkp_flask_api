from util.config import db
import datetime
import uuid, pytz
from datetime import datetime

from sqlalchemy import (
    Column,
    Double,
    ForeignKey,
    Null,
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
    path = Column(String(80), nullable=False)
    ext = Column(String(80), nullable=True)