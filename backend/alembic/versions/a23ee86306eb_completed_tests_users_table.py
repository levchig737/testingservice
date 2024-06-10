"""completed_tests_users table

Revision ID: a23ee86306eb
Revises: 53ad7421f161
Create Date: 2024-06-03 17:28:23.727290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a23ee86306eb'
down_revision: Union[str, None] = '53ad7421f161'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'completed_tests_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('test_id', sa.Integer, sa.ForeignKey('test.id'), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('scores', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('completed_tests_users')