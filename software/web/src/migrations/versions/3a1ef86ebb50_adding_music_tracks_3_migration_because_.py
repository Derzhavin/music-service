"""adding music tracks 3 migration, because forgot to add entities

Revision ID: 3a1ef86ebb50
Revises: 21116a58f1a9
Create Date: 2022-08-23 19:11:56.263533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a1ef86ebb50'
down_revision = '21116a58f1a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genres')
    # ### end Alembic commands ###
