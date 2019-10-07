"""empty message

Revision ID: 2f873c7ec57e
Revises: 
Create Date: 2019-10-07 00:11:18.590416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f873c7ec57e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Fleet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=45), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('password', sa.String(length=45), nullable=False),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('email_confirmation_sent_on', sa.DateTime(), nullable=True),
    sa.Column('email_confirmed', sa.Boolean(), nullable=True),
    sa.Column('email_confirmed_on', sa.DateTime(), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('last_logged_in', sa.DateTime(), nullable=True),
    sa.Column('current_logged_in', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(length=45), nullable=True),
    sa.Column('fleet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fleet_id'], ['Fleet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Vehicle',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('plate_number', sa.String(length=45), nullable=False),
    sa.Column('fleet_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fleet_fk'], ['Fleet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plate_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Vehicle')
    op.drop_table('User')
    op.drop_table('Fleet')
    # ### end Alembic commands ###