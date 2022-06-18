from AlphaDatabase import SESSION as YashuAlpha, BASE
from sqlalchemy import Column, Integer

class Users(BASE):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True)

   def __init__(self, uid)
       self.uid = uid

Users.__table__.create(checkfirst=True)

def add_user(id):
    user = YashviAlpha.query(Users).get(id)
    if not user:
        adder = Users(id)
        Yashualpha.add(adder)
        Yashualpha.commit()
    else:
        Yashualpha.close()
