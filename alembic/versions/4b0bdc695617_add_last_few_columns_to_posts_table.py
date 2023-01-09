"""add last few columns to posts table

Revision ID: 4b0bdc695617
Revises: ea462c33d10c
Create Date: 2023-01-09 20:19:28.098297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4b0bdc695617"
down_revision = "ea462c33d10c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
