"""Added bank info

Revision ID: 7e9be07a0f49
Revises: bf9d0a8b84b9
Create Date: 2022-02-02 09:07:06.210869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e9be07a0f49'
down_revision = 'bf9d0a8b84b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orphanage', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bank_info', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orphanage', schema=None) as batch_op:
        batch_op.drop_column('bank_info')

    # ### end Alembic commands ###
