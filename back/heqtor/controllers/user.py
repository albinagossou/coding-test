from heqtor.core import Session
from heqtor.models.user import User


def get_user(user_id: int):
    session = Session()
    user = session.query(User).get(user_id)
    if user is not None:
        user = user.get_small_data()
    session.close()
    return user


def update_user_data(user_id: int, phone: str = None):
    session = Session()
    try:
        user = session.query(User).get(user_id)
        if phone is not None:
            user.phone = phone
        session.commit()
        return user.get_small_data()
    except:
        session.rollback()
        return False
    finally:
        session.close()
