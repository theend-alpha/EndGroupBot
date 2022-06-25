from . import SESSION, BASE
from sqlalchemy import Column, Integer

class Sudo(BASE):
    __tablename__ = "sudo"

    user_id = Column(Integer, primary_key=True)
