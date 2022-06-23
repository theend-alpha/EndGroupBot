from sqlalchemy import Column, String

from . import BASE, SESSION


class Admins(BASE):
    __tablename__ = "admins"
    user_id = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, user_id, chat_id):
        self.user_id = str(user_id)
        self.chat_id = str(chat_id)


Admins.__table__.create(checkfirst=True)

def is_admin(str(user_id, str(chat_id)):
    admin = SESSION.query(Admins).get((str(user_id, str(chat_id))
    if admin:
        return True
    else:
        return False

def add_admin(str(user_id), str(chat_id)):
    admin = SESSION.query(Admins).get((str(user_id, str(chat_id))
    if not admin:
        adder = Admins(str(user_id), str(chat_id))
        SESSION.add(adder)
        SESSION.commit()
    else:
        SESSION.close()

