"""empty message

Revision ID: fc8ff785e1e1
Revises: 62909c6c04c8
Create Date: 2023-06-03 15:57:30.813191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8ff785e1e1'
down_revision = '62909c6c04c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('how_many', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('how_much', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_column('how_much')
        batch_op.drop_column('how_many')

    # ### end Alembic commands ###