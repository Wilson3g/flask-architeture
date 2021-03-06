"""empty message

Revision ID: cdf7428dfcff
Revises: 05d731072431
Create Date: 2020-05-08 09:49:00.452949

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cdf7428dfcff'
down_revision = '05d731072431'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('files_ibfk_1', 'files', type_='foreignkey')
    op.drop_column('files', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('files_ibfk_1', 'files', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
