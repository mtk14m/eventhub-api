"""rename paylod -> payload

Revision ID: rename_paylod_to_payload
Revises: daad964f6797
Create Date: 2026-02-01 16:45:00.000000

"""
from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = 'rename_paylod_to_payload'
down_revision: Union[str, Sequence[str], None] = 'daad964f6797'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename column 'paylod' to 'payload'
    op.alter_column('events', 'paylod', new_column_name='payload')


def downgrade() -> None:
    # Revert name back to 'paylod'
    op.alter_column('events', 'payload', new_column_name='paylod')
