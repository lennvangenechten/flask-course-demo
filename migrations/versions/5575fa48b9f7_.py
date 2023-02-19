"""empty message

Revision ID: 5575fa48b9f7
Revises: ab3d98b56160
Create Date: 2023-02-19 10:42:30.605292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5575fa48b9f7'
down_revision = 'ab3d98b56160'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint('email', ['email'])
    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('email', type_='unique')
        batch_op.drop_column('users', 'email')
    # ### end Alembic commands ###
