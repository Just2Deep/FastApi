"""add foreign key to posts table

Revision ID: ea462c33d10c
Revises: 7c23fe860453
Create Date: 2023-01-09 20:07:17.346922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ea462c33d10c"
down_revision = "7c23fe860453"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("owner_id", sa.Integer(), nullable=False),
    )
    op.create_foreign_key(
        "posts_users_fkey",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
