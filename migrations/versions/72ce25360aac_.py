"""empty message

Revision ID: 72ce25360aac
Revises: e5c615d35a78
Create Date: 2024-03-08 23:24:53.793987

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "72ce25360aac"
down_revision = "e5c615d35a78"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.alter_column(
            "price",
            existing_type=sa.REAL(),
            type_=sa.Float(precision=2),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.alter_column(
            "price",
            existing_type=sa.Float(precision=2),
            type_=sa.REAL(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
