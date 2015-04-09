from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

username = os.environ.get('PG_USER')
password = os.environ.get('PG_PASSWORD')
dbhost = os.environ.get('PG_HOST')
dbport = os.environ.get('PG_PORT')
db = os.environ.get('PG_DATABASE')

uri = 'postgres://'+username+':'+password+'@'+dbhost+':'+dbport+'/'+db
engine = create_engine(uri, convert_unicode=True,echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					 autoflush=False,
					 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import Flasktest.models
  Base.metadata.create_all(bind=engine)

