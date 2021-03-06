"""creating a column on the Profile table

Revision ID: ae34c861c0cc
Revises: 652ebc879d05
Create Date: 2018-09-19 10:07:26.601193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae34c861c0cc'
down_revision = '652ebc879d05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('support', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'support')
    # ### end Alembic commands ###
