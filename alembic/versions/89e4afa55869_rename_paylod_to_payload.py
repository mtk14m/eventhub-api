"""rename paylod to payload

Revision ID: 89e4afa55869
Revises: rename_paylod_to_payload
Create Date: 2026-02-01 16:50:09.485082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89e4afa55869'
down_revision: Union[str, Sequence[str], None] = 'rename_paylod_to_payload'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
