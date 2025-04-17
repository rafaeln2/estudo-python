"""Criacao tabelas

Revision ID: 019bfd2b02c5
Revises: 
Create Date: 2025-04-16 16:04:06.935332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from teste.UsuarioCRUDTest import criar_base


# revision identifiers, used by Alembic.
revision: str = '019bfd2b02c5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    criar_base()
    pass


def downgrade() -> None:
    op.execute("""
               DROP TABLE IF EXISTS usuarios;
               DROP TABLE IF EXISTS cursos;
               DROP TABLE IF EXISTS usuario_curso;""")
    pass
