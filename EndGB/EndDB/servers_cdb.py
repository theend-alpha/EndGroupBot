from . import SESSION, BASE
from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import BigInteger
import threading 

class Served(BASE):
    __tablename__ = "served"

    chat_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

class Users(BASE):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id

Users.__table__.create(checkfirst=True)

Served.__table__.create(checkfirst=True)

Served_IL = threading.RLock()

Users_IL = threading.RLock()

def add_served_chat(chat_id):
    with Served_IL:
        try:
            SESSION.add(Served(chat_id))
            SESSION.commit()
        finally:
            SESSION.close()

def is_served_chat(chat_id):
    served = SESSION.query(Served).get(chat_id)
    if served:
        return True
    else:
        return False

def add_private_user(user_id):
    with Users_IL:
        try:
            SESSION.add(Users(user_id))
            SESSION.commit()
        finally:
            SESSION.close()

def is_private_user(user_id):
    served = SESSION.query(Users).get(user_id)
    if served:
        return True
    else:
        return False
