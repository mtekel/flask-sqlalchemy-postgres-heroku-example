import os
from Flasktest import app
from Flasktest.database import init_db

@app.before_first_request
def init_stuff():
  init_db()

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
