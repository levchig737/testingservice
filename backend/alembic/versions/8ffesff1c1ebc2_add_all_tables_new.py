from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7389vjsefjs'
down_revision = '752cd04ffebe'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('owner', sa.String(), nullable=False),
        sa.Column('theme', sa.String(), nullable=False),
        sa.Column('min_score', sa.Integer(), nullable=False),
        sa.Column('max_score', sa.Integer(), nullable=False)
    )

    op.create_table('answer',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('answer1', sa.String(), nullable=False),
        sa.Column('answer2', sa.String(), nullable=False),
        sa.Column('answer3', sa.String(), nullable=True),
        sa.Column('answer4', sa.String(), nullable=True),
        sa.Column('answer5', sa.String(), nullable=True),
        sa.Column('answer6', sa.String(), nullable=True),
        sa.Column('answer7', sa.String(), nullable=True),
        sa.Column('answer8', sa.String(), nullable=True),
        sa.Column('answer9', sa.String(), nullable=True),
        sa.Column('answer10', sa.String(), nullable=True),
        sa.Column('question_id', sa.Integer(), sa.ForeignKey('question.id'), nullable=False)
    )

    op.create_table('right_answer',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('answer1', sa.Boolean(), nullable=False),
        sa.Column('answer2', sa.Boolean(), nullable=True),
        sa.Column('answer3', sa.Boolean(), nullable=True),
        sa.Column('answer4', sa.Boolean(), nullable=True),
        sa.Column('answer5', sa.Boolean(), nullable=True),
        sa.Column('answer6', sa.Boolean(), nullable=True),
        sa.Column('answer7', sa.Boolean(), nullable=True),
        sa.Column('answer8', sa.Boolean(), nullable=True),
        sa.Column('answer9', sa.Boolean(), nullable=True),
        sa.Column('answer10', sa.Boolean(), nullable=True),
        sa.Column('question_id', sa.Integer(), sa.ForeignKey('question.id'), nullable=False)
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('right_answer')
    op.drop_table('answer')
    op.drop_table('test')