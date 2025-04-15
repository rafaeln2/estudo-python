"""insert usuario Rafael

Revision ID: 0eb53089556b
Revises: 09f7f06a2317
Create Date: 2025-04-15 17:06:22.635697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0eb53089556b'
down_revision: Union[str, None] = '09f7f06a2317'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.execute(
        """
        INSERT INTO public.usuarios
            (id, nome, ativo, email)
        VALUES
            (nextval('usuarios_id_seq'::regclass), 'Rafael', true, 'fed@yahoo.com');
        """
        )


def downgrade() -> None:
        op.execute(
        """
        DELETE FROM usuarios u WHERE u.nome = 'Rafael';
        """
        )
