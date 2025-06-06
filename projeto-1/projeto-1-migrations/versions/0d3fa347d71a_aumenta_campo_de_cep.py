"""aumenta campo de cep

Revision ID: 0d3fa347d71a
Revises: f185b4c36b39
Create Date: 2025-04-29 18:01:53.437644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0d3fa347d71a'
down_revision: Union[str, None] = 'f185b4c36b39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('viacep', 'cep',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.String(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('viacep', 'cep',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=8),
               existing_nullable=False)
    # ### end Alembic commands ###
