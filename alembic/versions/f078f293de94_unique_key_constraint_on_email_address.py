"""unique key constraint on email_address

Revision ID: f078f293de94
Revises: 945afb9b8916
Create Date: 2019-08-01 11:09:18.332478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f078f293de94'
down_revision = '945afb9b8916'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(250), nullable=False),
        sa.Column('last_name', sa.String(250), nullable=False),
        sa.Column('email_address', sa.String(250), nullable=False),
        sa.Column('phone_number', sa.String(250), nullable=False),
        sa.UniqueConstraint('email_address')
    )


def downgrade():
    op.drop_table('users')