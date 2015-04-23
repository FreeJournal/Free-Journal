from sqlalchemy import create_engine
from .models import DecBase
from . import config


def connect_db():
    """
    Initialize connection to the database engine
    :return: newly created engine
    """
    engine = create_engine(config.DB_URL)
    return engine


def setup_db(engine):
    """
    Creates and initializes necessary database tables
    :param engine: the database engine to use
    :return:
    """
    DecBase.metadata.create_all(engine)
