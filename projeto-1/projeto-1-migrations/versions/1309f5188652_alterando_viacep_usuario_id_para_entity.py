"""alterando viacep usuario id para entity

Revision ID: 1309f5188652
Revises: 53ac6ae91299
Create Date: 2025-04-29 17:24:34.562222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '1309f5188652'
down_revision: Union[str, None] = '53ac6ae91299'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viacep', sa.Column('usuario', sa.Integer(), nullable=True))
    op.drop_constraint('viacep_usuario_id_fkey', 'viacep', type_='foreignkey')
    op.create_foreign_key(None, 'viacep', 'usuarios', ['usuario'], ['id'])
    op.drop_column('viacep', 'usuario_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viacep', sa.Column('usuario_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'viacep', type_='foreignkey')
    op.create_foreign_key('viacep_usuario_id_fkey', 'viacep', 'usuarios', ['usuario_id'], ['id'])
    op.drop_column('viacep', 'usuario')
    # ### end Alembic commands ###
