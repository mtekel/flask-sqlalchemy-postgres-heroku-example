from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from flask import current_app as app
import os

username = os.environ.get('PG_USER', 'demo')
password = os.environ.get('PG_PASSWORD', 'demo')
dbhost = os.environ.get('PG_HOST', 'localhost')
dbport = os.environ.get('PG_PORT', '5432')
db = os.environ.get('PG_DATABASE', 'demo')

uri = 'postgres://'+username+':'+password+'@'+dbhost+':'+dbport+'/'+db
engine = create_engine(uri, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import Flasktest.models
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as e:
        app.logger.error(e)
