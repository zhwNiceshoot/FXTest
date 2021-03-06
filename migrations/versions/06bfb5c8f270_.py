"""empty message

Revision ID: 06bfb5c8f270
Revises: 2488b2a0a217
Create Date: 2019-04-23 08:54:15.345663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06bfb5c8f270'
down_revision = '2488b2a0a217'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('interfacetests', sa.Column('is_ci', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'tstresults', type_='foreignkey')
    op.add_column('tasks', sa.Column('taskdesc', sa.TEXT(length=252), nullable=True))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'projects', type_='unique')
    op.drop_constraint(None, 'interfacetests', type_='foreignkey')
    op.drop_column('interfacetests', 'is_ci')
    # ### end Alembic commands ###
