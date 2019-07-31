"""change table name

Revision ID: ce90fa5ed691
Revises: a2aed28f954f
Create Date: 2019-07-31 12:31:36.547471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce90fa5ed691'
down_revision = 'a2aed28f954f'
branch_labels = None
depends_on = None


def upgrade():

 op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(250), nullable=False),
        sa.Column('last_name', sa.String(250), nullable=False),
        sa.Column('email_address', sa.String(250), nullable=False),
        sa.Column('phone_number', sa.String(250), nullable=False)
    )


def downgrade():
    op.drop_table('users')
