from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base, IdPkMixin
from .company import Company


class User(Base, IdPkMixin):
    # Supprimer le mot de passe
    def get_small_data(self):
        dupwd = super.get_small_data()
        del dupwd['password']
        return dupwd
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(13))
    company_id = Column(Integer, ForeignKey(Company.id))
    company = relationship(Company, backref="users")
