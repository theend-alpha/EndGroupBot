from . import SESSION, BASE
from sqlalchemy import Column, Integer

class Block(BASE):
    __tablename__ = "block"

    i = Column(Integer, primary_key=True)

    def __init__(self, i):
        self.i = i

Block.__table__.create(checkfirst=True)

def block_user(i):
    is_sudo = SESSION.query(Block).get(i)
    if not is_sudo:
        adder = Block(i)
        SESSION.add(adder)
        SESSION.commit()
    else:
        SESSION.close()

def unblock_user(i):
    is_sudo = SESSION.query(Block).get(i)
    if is_sudo:
        SESSION.delete(is_sudo)
        SESSION.commit()
    else:
        SESSION.close()

def is_blocked(i):
    sudo = SESSION.query(Block).get(i)
    if sudo:
        return True
    else:
        return False

def clr_all_blocked():
    sudos = SESSION.query(Block).all()
    SUDOS = []
    for sudo in sudos:
        SUDOS.append(sudo.i)
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
