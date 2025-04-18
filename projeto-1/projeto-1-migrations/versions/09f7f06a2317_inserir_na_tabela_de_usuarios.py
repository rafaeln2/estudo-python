"""Inserir na tabela de usuarios

Revision ID: 09f7f06a2317
Revises: 8fca8dc342de
Create Date: 2025-04-14 16:22:52.705967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# import sqlmodel
from models import Usuario


# revision identifiers, used by Alembic.
revision: str = '09f7f06a2317'
down_revision: Union[str, None] = '8fca8dc342de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO public.usuarios
            (id, nome, ativo, email)
        VALUES
            (nextval('usuarios_id_seq'::regclass), 'Teste Alembic', false, 'email@teste.com');
        """
    )


def downgrade() -> None:
        op.execute(
        """
        DELETE FROM usuarios u WHERE u.nome = 'Teste Alembic';
        """
    )
