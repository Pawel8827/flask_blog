"""empty message

Revision ID: 63214fafc51a
Revises: 2fd8c660e24a
Create Date: 2020-08-03 14:58:19.671739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63214fafc51a'
down_revision = '2fd8c660e24a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'referat', 'wydzial', ['wydzial_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'referat', type_='foreignkey')
    # ### end Alembic commands ###
