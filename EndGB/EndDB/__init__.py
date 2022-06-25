from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from .sudos_cdb import *
from .blocks_cdb import *

DATABASE_URL = os.environ.get('DATABASE_URL', None)

DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
