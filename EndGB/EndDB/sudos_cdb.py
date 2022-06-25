from . import SESSION, BASE
from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import BigInteger

class SUDO(BASE):
    __tablename__ = "sudousers"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

SUDO.__table__.create(checkfirst=True)

SUDO_IL = threading.RLock()

def add_sudo(id):
    with SUDO_IL:
        is_sudo = SESSION.query(SUDO).get(id)
        if not is_sudo:
            adder = SUDO(id)
            SESSION.add(adder)
            SESSION.commit()
        else:
            SESSION.close()
    
def del_sudo(id):
    with SUDO_IL:
        is_sudo = SESSION.query(SUDO).get(id)
        if is_sudo:
            SESSION.delete(is_sudo)
            SESSION.commit()
        else:
            SESSION.close()

def list_all_sudos():
    sudos = SESSION.query(SUDO).all()
    try:
        return sudos
    finally:
        SESSION.close()

def is_sudo(id):
    sudo = SESSION.query(SUDO).get(id)
    if sudo:
        return True
    else:
        return False

def clr_all_sudos():
    OMFOO = []
    sudos = SESSION.query(SUDO).all()
    for sudo in sudos:
        OMFOO.append(sudo.id)
    for baka in OMFOO:
        shivi = SESSION.query(SUDO).get(baka)
        SESSION.delete(shivi)
        SESSION.commit()
