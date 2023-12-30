from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


url_obj = URL.create(
    'postgresql+pg8000',
    username=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    database=DB_NAME,
    port=DB_PORT,
)

engine = create_engine(url_obj)
session = sessionmaker(engine)
class Base(DeclarativeBase):
    pass


def get_db():
    db = session()
    
    try:
        yield db
    finally:
        db.close()