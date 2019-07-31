"""create users table

Revision ID: a2aed28f954f
Revises: 
Create Date: 2019-07-31 11:56:27.654836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2aed28f954f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(250), nullable=False),
        sa.Column('last_name', sa.String(250), nullable=False)
    )


def downgrade():
    op.drop_table('user')
