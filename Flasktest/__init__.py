from __future__ import with_statement
from contextlib import closing
from Flasktest.database import db_session
from flask import Flask
from flask.ext.stats import Stats

import Flasktest.views

#configuration
DATABASE = '/tmp/flasktest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# Flask stats configuration
# STATS_HOSTNAME
app.config.from_envvar('STATS_HOSTNAME')
# STATS_PORT
app.config.from_envvar('STATS_PORT')
# STATS_BASE_KEY
app.config.from_envvar('STATS_BASE_KEY')

# Initialise flask-metrics
stats = Stats().init_app(app)

@app.teardown_request
def teardown_request(exception):
  db_session.remove()

