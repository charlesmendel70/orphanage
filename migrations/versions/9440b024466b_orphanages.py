"""Orphanages

Revision ID: 9440b024466b
Revises: 
Create Date: 2022-01-08 16:29:45.828904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9440b024466b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orphanage', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('orphanage', sa.Column('email', sa.String(length=120), nullable=True))
    op.add_column('orphanage', sa.Column('students', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_orphanage_email'), 'orphanage', ['email'], unique=True)
    op.create_index(op.f('ix_orphanage_name'), 'orphanage', ['name'], unique=True)
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.VARCHAR(length=200), nullable=True))
    op.drop_index(op.f('ix_orphanage_name'), table_name='orphanage')
    op.drop_index(op.f('ix_orphanage_email'), table_name='orphanage')
    op.drop_column('orphanage', 'students')
    op.drop_column('orphanage', 'email')
    op.drop_column('orphanage', 'name')
    # ### end Alembic commands ###
