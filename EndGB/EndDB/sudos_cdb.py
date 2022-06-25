from . import SESSION, BASE
from sqlalchemy import Column, Integer

class Sudo(BASE):
    __tablename__ = "sudo"

    user_id = Column(Integer, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user.id

Sudo.__table__.create(checkfirst=True)

def add_sudo(i):
    is_sudo = SESSION.query(Sudo).get(i)
    if not is_sudo:
        adder = Sudo(i)
        SESSION.add(adder)
        SESSION.commit()
    else:
        SESSION.close()

def del_sudo(i):
    is_sudo = SESSION.query(Sudo).get(i)
    if is_sudo:
        SESSION.delete(is_sudo)
        SESSION.commit()
    else:
        SESSION.close()

def is_sudo(i):
    sudo = SESSION.query(Sudo).get(i)
    if sudo:
        return True
    else:
        return False

def clr_all_sudos():
    sudos = SESSION.query(Sudo).all()
    SUDOS = []
    for sudo in sudos:
        SUDOS.append(sudo.i)
        for SUDO in SUDOS:
            lel = SESSION.query(Sudo).get(SUDO)
            SESSION.delete(lel)
            SESSION.commit()

def list_all_sudos():
    sudos = SESSION.query(Sudo).all()
    try:
        return sudos
    finally:
        SESSION.close()

