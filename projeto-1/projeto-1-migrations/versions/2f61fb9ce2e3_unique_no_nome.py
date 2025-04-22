"""unique no nome

Revision ID: 2f61fb9ce2e3
Revises: 4486d196602a
Create Date: 2025-04-19 17:30:58.570279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '2f61fb9ce2e3'
down_revision: Union[str, None] = '4486d196602a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('usuarios', 'nome', unique=True)
    


def downgrade() -> None:
    op.alter_column('usuarios', 'nome', unique=False)
