"""empty message

Revision ID: 14f2bf7f4bcd
Revises: 
Create Date: 2023-12-30 14:25:21.366239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f2bf7f4bcd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('contents', sa.Text(), nullable=True),
    sa.Column('writer', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
