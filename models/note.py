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
    from models.user import User


idpk = Annotated[int, mapped_column(primary_key=True)]

class Note(Base):
    __tablename__ = 'notes'
    
    id: Mapped[idpk]
    title: Mapped[str] = mapped_column(nullable=False)
    subtitle: Mapped[str] = mapped_column(nullable=True)
    introduction: Mapped[str] = mapped_column(nullable=False)
    main_text: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship(backref='users')
    