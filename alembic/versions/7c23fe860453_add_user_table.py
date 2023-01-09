"""add user table

Revision ID: 7c23fe860453
Revises: 5ce4e37d5a0b
Create Date: 2023-01-09 19:56:50.517995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7c23fe860453"
down_revision = "5ce4e37d5a0b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("password", sa.String, nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
