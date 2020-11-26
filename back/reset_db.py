from heqtor.core import config, Session
from heqtor.models.base import Base
from heqtor.models import *


def reset_db():
    session = Session()
    if config["env"] == "development":
        Base.metadata.drop_all()
    Base.metadata.create_all()
    session.commit()
    session.close()


if __name__ == "__main__":
    reset_db()
