"""merge upstream and lazy history migration heads

Revision ID: f3a4b5c6d7e8
Revises: d4c1a8e37b62, e2f4a6b8c0d1
Create Date: 2026-08-31 04:50:00.000000

"""

from collections.abc import Sequence


# revision identifiers, used by Alembic.
revision: str = 'f3a4b5c6d7e8'
down_revision: tuple[str, str] = ('d4c1a8e37b62', 'e2f4a6b8c0d1')
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
