"""upgrade test

Revision ID: 752cd04ffebe
Revises: f05f40dc80ac
Create Date: 2024-05-31 16:46:04.008330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '752cd04ffebe'
down_revision: Union[str, None] = 'f05f40dc80ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('question',
    #     sa.Column('id', sa.Integer(), nullable=False),
    #     sa.Column('content', sa.Text(), nullable=True),
    #     sa.Column('test_id', sa.Integer(), nullable=True),
    #     sa.PrimaryKeyConstraint('id')
    # )
    # ### end Alembic commands ###

def downgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('question')
    # ### end Alembic commands ###
