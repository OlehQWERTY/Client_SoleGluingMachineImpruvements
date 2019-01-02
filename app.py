# $ pip install Flask
# $ FLASK_APP=client.py flask run
#  * Running on http://localhost:5000/

from flask import Flask, render_template, url_for, flash, redirect
from config import Configuration
# from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SECRET_KEY'] = '1234'
# app.run(debug=True)


