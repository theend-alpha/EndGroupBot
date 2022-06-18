from AlphaDatabase import SESSION as YashuAlpha, BASE
from sqlalchemy import Column, Integer

class Users(BASE):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True)

   def __init__(self, uid)
       self.uid = uid

Users.__table__.create(checkfirst=True)
