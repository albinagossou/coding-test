from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr
import re

from heqtor.core import db


class Base:
    @declared_attr
    def __tablename__(cls):
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower() + "s"

    def get_small_data(self):
        return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())


Base = declarative_base(cls=Base, bind=db)


class IdPkMixin:
    id = Column(Integer, primary_key=True)
