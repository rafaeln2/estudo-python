"""atualizar viacep unidade

Revision ID: 421561b90e73
Revises: 5339290e7b2c
Create Date: 2025-04-29 16:39:52.457189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '421561b90e73'
down_revision: Union[str, None] = '5339290e7b2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viacep', sa.Column('unidade', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('viacep', 'unidade')
    # ### end Alembic commands ###
