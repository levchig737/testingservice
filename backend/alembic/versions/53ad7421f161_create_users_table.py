"""create users table

Revision ID: 53ad7421f161
Revises: 9febf2d1925a
Create Date: 2024-06-03 15:24:10.534844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53ad7421f161'
down_revision: Union[str, None] = 'c727ab87b879'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('blocked_flag', sa.Boolean, nullable=False),
        sa.Column('role', sa.Enum('admin', 'user', name='userrole'), nullable=False),
        sa.Column('email', sa.String(length=255), unique=True, nullable=False),
        sa.Column('hashed_password', sa.String(length=1024), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True, nullable=False),
        sa.Column('is_superuser', sa.Boolean, default=True, nullable=False),
        sa.Column('is_verified', sa.Boolean, default=True, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
