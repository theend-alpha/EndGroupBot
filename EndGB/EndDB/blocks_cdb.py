from . import SESSION, BASE
from sqlalchemy import Column, Integer

class Block(BASE):
    __tablename__ = "block"

    id = Column(Integer, primary_key=True)

    def __init__(self, id):
        self.id = id

Block.__table__.create(checkfirst=True)

def block_user(id):
    is_sudo = SESSION.query(Block).get(id)
    if not is_sudo:
        adder = Block(id)
        SESSION.add(adder)
        SESSION.commit()
    else:
        SESSION.close()

def unblock_user(id):
    is_sudo = SESSION.query(Block).get(id)
    if is_sudo:
        SESSION.delete(is_sudo)
        SESSION.commit()
    else:
        SESSION.close()

def is_blocked(id):
    sudo = SESSION.query(Block).get(id)
    if sudo:
        return True
    else:
        return False

def clr_all_blocked():
    sudos = SESSION.query(Block).all()
    SUDOS = []
    for sudo in sudos:
        SUDOS.append(sudo.id)
    for SUDO in SUDOS:
        lel = SESSION.query(Block).get(SUDO)
        SESSION.delete(lel)
        SESSION.commit()

def list_all_blocked():
    sudos = SESSION.query(Block).all()
    try:
        return sudos
    finally:
        SESSION.close()
