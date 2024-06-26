"""set bool right_answers

Revision ID: f05f40dc80ac
Revises: 8f78f1c1ebc2
Create Date: 2024-05-31 10:49:42.270169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f05f40dc80ac'
down_revision: Union[str, None] = '8f78f1c1ebc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('right_answer', 'answer1',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=False,
               postgresql_using='answer1::boolean')
    op.alter_column('right_answer', 'answer2',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer2::boolean')
    op.alter_column('right_answer', 'answer3',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer3::boolean')
    op.alter_column('right_answer', 'answer4',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer4::boolean')
    op.alter_column('right_answer', 'answer5',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer5::boolean')
    op.alter_column('right_answer', 'answer6',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer6::boolean')
    op.alter_column('right_answer', 'answer7',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer7::boolean')
    op.alter_column('right_answer', 'answer8',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer8::boolean')
    op.alter_column('right_answer', 'answer9',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer9::boolean')
    op.alter_column('right_answer', 'answer10',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True,
               postgresql_using='answer10::boolean')
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('right_answer', 'answer10',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer10::varchar')
    op.alter_column('right_answer', 'answer9',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer9::varchar')
    op.alter_column('right_answer', 'answer8',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer8::varchar')
    op.alter_column('right_answer', 'answer7',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer7::varchar')
    op.alter_column('right_answer', 'answer6',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer6::varchar')
    op.alter_column('right_answer', 'answer5',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer5::varchar')
    op.alter_column('right_answer', 'answer4',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer4::varchar')
    op.alter_column('right_answer', 'answer3',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer3::varchar')
    op.alter_column('right_answer', 'answer2',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True,
               postgresql_using='answer2::varchar')
    op.alter_column('right_answer', 'answer1',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               postgresql_using='answer1::varchar')
    # ### end Alembic commands ###
