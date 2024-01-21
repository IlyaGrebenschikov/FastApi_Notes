"""create_table

Revision ID: a435336623ae
Revises: 779bba298d17
Create Date: 2024-01-21 06:19:38.811443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a435336623ae'
down_revision: Union[str, None] = '779bba298d17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
