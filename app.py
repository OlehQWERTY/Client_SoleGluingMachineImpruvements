# $ pip install Flask
# $ FLASK_APP=client.py flask run
#  * Running on http://localhost:5000/

from flask import Flask
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
# app.run(debug=True)


