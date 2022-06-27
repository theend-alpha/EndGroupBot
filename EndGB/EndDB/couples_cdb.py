from . import SESSION, BASE
from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import BigInteger
import threading 

class Couples(BASE):
    __tablename__ = "couples"

    c1_id = Column(BigInteger, primary_key=True)
    c2_id = Column(BigInteger, primary_key=True)
    date = Column(BigInteger, primary_key=True)
    month = Column(BigInteger, primary_key=True)
    year = Column(BigInteger, primary_key=True)

    def __init__(self, c1_id, c2_id, date, month, year):
        self.c1_id = c1_id
        self.c2_id = c2_id
        self.date = date
        self.month = month 
        self.year = year

class CoupleCheck(BASE):
    __tablename__ = "couplecheck"

    date = Column(BigInteger, primary_key=True)
    month = Column(BigInteger, primary_key=True)
    year = Column(BigInteger, primary_key=True)

    def __init__(self, date, month, year):
        self.date = date
        self.month = month 
        self.year = year

Couples.__table__.create(checkfirst=True)

CoupleCheck.__table__.create(checkfirst=True)

Couples_IL = threading.RLock()

CoupleCheck_IL = threading.RLock()

def couple_of_the_day(c1_id, c2_id, date, month, year):
    with Couples_IL:
        try:
            SESSION.add(Couples(c1_id, c2_id, date, month, year)
            SESSION.commit()
        except:
            SESSION.close()

def couple_found(date, month, year);
    couple_found = SESSION.query(CoupleCheck).get(date, month, year)
    if couple_found:
        return True
    else:
        return False 
