from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from app.config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD


url_obj = URL.create(
    'postgresql+pg8000',
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    database=POSTGRES_DB,
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
