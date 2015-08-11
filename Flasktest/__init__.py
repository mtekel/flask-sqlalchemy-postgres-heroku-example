from __future__ import with_statement
from contextlib import closing
from Flasktest.database import db_session
from Flasktest.database import init_db
from flask import Flask
from flask.ext.stats import Stats
import os
import logging

# configuration
DATABASE = '/tmp/flasktest.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

import Flasktest.views


# Flask stats configuration
# STATS_HOSTNAME
app.config['STATS_HOSTNAME'] = os.environ.get('STATS_HOSTNAME', "")
# STATS_PORT
app.config['STATS_PORT'] = os.environ.get('STATS_PORT', "")
# STATS_BASE_KEY
app.config['STATS_BASE_KEY'] = os.environ.get('STATS_BASE_KEY', "")

# Initialise flask-metrics, only if connection setup
if app.config['STATS_HOSTNAME'] != "":
    stats = Stats().init_app(app)


@app.before_first_request
def init_stuff():
    init_db()


@app.teardown_request
def teardown_request(exception):
    db_session.remove()
