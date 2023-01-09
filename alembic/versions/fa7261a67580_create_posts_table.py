"""create posts table

Revision ID: fa7261a67580
Revises: 
Create Date: 2023-01-08 21:17:25.813959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fa7261a67580"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
