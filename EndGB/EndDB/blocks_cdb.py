from . import SESSION, BASE
from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import BigInteger
import threading 

class Block(BASE):
    __tablename__ = "blocks"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

Block.__table__.create(checkfirst=True)

Block_IL = threading.RLock()

def block_user(id):
    with Block_IL:
        is_sudo = SESSION.query(Block).get(id)
        if not is_sudo:
            adder = Block(id)
            SESSION.add(adder)
            SESSION.commit()
        else:
            SESSION.close()
    
def unblock_user(id):
    with Block_IL:
        is_sudo = SESSION.query(Block).get(id)
        if is_sudo:
            SESSION.delete(is_sudo)
            SESSION.commit()
        else:
            SESSION.close()

def list_all_blocked():
    sudos = SESSION.query(Block).all()
    try:
        return sudos
    finally:
        SESSION.close()

def is_blocked(id):
    sudo = SESSION.query(Block).get(id)
    if sudo:
        return True
    else:
        return False
