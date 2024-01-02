from typing import Annotated, List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from database import Base

import typing
if typing.TYPE_CHECKING:
    from models.note import Note


idpk = Annotated[int, mapped_column(primary_key=True)]

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[idpk]
    name: Mapped[str]
    note: Mapped[List['Note']] = relationship(backref='notes')
    