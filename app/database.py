from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from app.config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT


url_obj = URL.create(
    'postgresql+psycopg',
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    database=POSTGRES_DB,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
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
