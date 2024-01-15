from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.app.database import Base

import typing

if typing.TYPE_CHECKING:
    from src.app.notes import NoteModels as Note


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    note: Mapped[List['Note']] = relationship('Note')
