"""reset table

Revision ID: 945afb9b8916
Revises: ce90fa5ed691
Create Date: 2019-07-31 12:35:11.820837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '945afb9b8916'
down_revision = 'ce90fa5ed691'
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
