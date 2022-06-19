from EndFW.AlphaDatabase import SESSION as YashuAlpha, BASE
from sqlalchemy import Column, Integer

class Users(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    def __init__(self, id):
        self.id = id

class PUsers(BASE):
    __tablename__ = "pusers"

    id = Column(Integer, primary_key=True)

    def __init__(self, id):
        self.id = id


Users.__table__.create(checkfirst=True)

PUsers.__table__.create(checkfirst=True)


def private_user(id):
    user = YashuAlpha.query(PUsers).get(id)
    if not user:
        adder = PUsers(id)
        YashuAlpha.add(adder)
        YashuAlpha.commit()
    else:
        YashuAlpha.close()

def get_pusers():
    try:
        return YashuAlpha.query(PUsers).all()
    finally:
        YashuAlpha.close()

def get_users():
    try:
        return YashuAlpha.query(Users).all()
    finally:
        YashuAlpha.close()

def add_user(id):
    user = YashuAlpha.query(Users).get(id)
    if not user:
        adder = Users(id)
        YashuAlpha.add(adder)
        YashuAlpha.commit()
    else:
        YashuAlpha.close()
