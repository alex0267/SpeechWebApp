"""First migration

Revision ID: 90cc4d7dc7b1
Revises: 
Create Date: 2021-01-12 09:15:44.328534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from ser_api.model.record_model import Record
from ser_api.model.deleted_model import Deleted
from ser_api.model.sentence_model import Sentence
from ser_api.utils.config import config, CONFIG_ENV

# revision identifiers, used by Alembic.
revision = '90cc4d7dc7b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    engine = create_engine(config[CONFIG_ENV].db_url_string())
    # Create database if it does not exist.
    if not database_exists(engine.url):
        create_database(engine.url)

    if not engine.dialect.has_table(engine,Sentence.__tablename__):
        op.create_table(
            Sentence.__tablename__,
            sa.Column('id', Integer, primary_key=True,index=True),
            sa.Column('sentence', String(100), nullable=False,unique=True),
        )
        session.commit()
    if not engine.dialect.has_table(engine,Deleted.__tablename__):
        op.create_table(
            'deleted',
            Column('id', Integer, primary_key=True,index=True),
            Column('uuid', String(50), nullable=False),
            Column('timestamp', String(50), nullable=False),
        )
    if not engine.dialect.has_table(engine,Record.__tablename__):
        op.create_table(
            'record',
            Column('id', Integer, primary_key=True,index=True),
            Column('record_url', String(100), nullable=False),
            Column('emotion', String(50), nullable=False),
            Column('timestamp', DateTime(), nullable=False),
            Column('uuid', String(50), nullable=False),
            sa.Column('sentence_id', Integer, nullable=False),
            sa.ForeignKeyConstraint(('sentence_id',), ['sentence.id'],),
        )
    session.commit()
    s_sentences = ["Les enfants sont sortis dans le jardin malgr?? la pluie.",
    "Les joueurs n???ont pas encore termin?? leur pr??paration.",
    "Alex se tenait dans le salon lorsqu???il l???a aper??u.",
    "Le sapin de No??l a plus de guirlandes que d?????pines.",
    "Cette peinture ne laisse personne sortir indemne de la pi??ce.",
    "Le num??rique a compl??tement transform?? la soci??t??.",
    "Les ??coliers peuvent se promener librement en centre ville.",
    "Voyager n???a jamais autant compt?? pour mes parents.",
    "Regarder ce film a d??finitivement chang?? ma fa??on de r??pondre au t??l??phone.",
    "Sauter ou plonger, dans certaines situations, il faut faire un choix."]
    sentences = [Sentence(sentence=_sentence) for _sentence in s_sentences]
    session.add_all(sentences)
    session.commit()

def downgrade():
    op.drop_table('deleted')
    op.drop_table('record')
    op.drop_table('sentence')
