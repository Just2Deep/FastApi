"""add content column to posts table

Revision ID: 5ce4e37d5a0b
Revises: fa7261a67580
Create Date: 2023-01-08 21:27:43.934697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5ce4e37d5a0b"
down_revision = "fa7261a67580"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
