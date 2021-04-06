"""add fields

Revision ID: d515502f359b
Revises: 41559db5787d
Create Date: 2021-04-04 13:25:27.766922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd515502f359b'
down_revision = '41559db5787d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('california', sa.Column('recovered', sa.Integer(), nullable=True))
    op.add_column('california', sa.Column('total_tested', sa.Integer(), nullable=True))
    op.add_column('la_county', sa.Column('recovered', sa.Integer(), nullable=True))
    op.add_column('la_county', sa.Column('total_tested', sa.Integer(), nullable=True))
    op.add_column('orange_county', sa.Column('recovered', sa.Integer(), nullable=True))
    op.add_column('united_states', sa.Column('total_tested', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('united_states', 'total_tested')
    op.drop_column('orange_county', 'recovered')
    op.drop_column('la_county', 'total_tested')
    op.drop_column('la_county', 'recovered')
    op.drop_column('california', 'total_tested')
    op.drop_column('california', 'recovered')
    # ### end Alembic commands ###