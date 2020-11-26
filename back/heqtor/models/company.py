from sqlalchemy import Column, String

from .base import Base, IdPkMixin


class Company(Base, IdPkMixin):
    name = Column(String(35), nullable=False)
    siren = Column(String(9), unique=True, nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(13), nullable=False)
