"""Nullable tables"

Revision ID: 62985ab5f2f2
Revises: 2ee3c34f90ff
Create Date: 2025-04-04 19:41:08.776193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62985ab5f2f2'
down_revision: Union[str, None] = '2ee3c34f90ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts', 'desc',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'desc',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###