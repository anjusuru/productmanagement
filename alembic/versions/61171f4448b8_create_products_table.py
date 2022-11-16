"""create products table

Revision ID: 61171f4448b8
Revises: 
Create Date: 2022-11-16 16:36:29.587825

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "61171f4448b8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False, unique=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("brand", sa.String(100)),
        sa.Column("price", sa.Float),
        sa.Column("quantity", sa.Integer),
    )


def downgrade() -> None:
    pass
