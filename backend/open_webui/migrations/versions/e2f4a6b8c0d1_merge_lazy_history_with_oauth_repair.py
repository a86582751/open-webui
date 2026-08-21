"""merge lazy history storage with oauth repair

Revision ID: e2f4a6b8c0d1
Revises: b8f1c2d3e4a5, 6d09d1bf1f23
Create Date: 2026-08-21 09:00:00.000000

"""

from collections.abc import Sequence

revision: str = 'e2f4a6b8c0d1'
down_revision: tuple[str, str] = ('b8f1c2d3e4a5', '6d09d1bf1f23')
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
