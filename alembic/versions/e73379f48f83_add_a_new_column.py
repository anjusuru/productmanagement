"""add a new column

Revision ID: e73379f48f83
Revises: 61171f4448b8
Create Date: 2022-11-16 22:04:04.926229

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "e73379f48f83"
down_revision = "61171f4448b8"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("products", sa.Column("category", sa.String))


def downgrade():
    op.drop_column("products", "category")
