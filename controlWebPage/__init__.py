# template language: Jinja 2

from flask import Flask
from controlWebPage.config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # db
db = SQLAlchemy(app)

from controlWebPage import routes