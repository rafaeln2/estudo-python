"""Criar tabela usuarios

Revision ID: 8fca8dc342de
Revises: 
Create Date: 2025-04-14 11:54:05.083263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
# import sqlmodel
from models import Usuario


# revision identifiers, used by Alembic.
revision: str = '8fca8dc342de'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # op.create_table(
    #     'usuarios',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('nome', sa.String, nullable=False),
    #     sa.Column('email', sa.String, nullable=False),
    #     sa.Column('ativo', sa.Boolean, default=True),
    # )
    print("primeira migração passou")

def downgrade() -> None:
    """Downgrade schema."""
    # op.drop_table("usuarios")
