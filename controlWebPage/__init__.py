# template language: Jinja 2

from flask import Flask
from controlWebPage.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import mysql.connector as mSql  # my sql official py connect


try:
	mydb = mSql.connect(
	  host="172.16.2.142",
	  user="monitor",
	  passwd="password",
	  database="sole_1"
	)

	mycursor = mydb.cursor(buffered=True)

except mSql.Error as err:
	# make something further
	print("Failed connecting to database: {}".format(err))

app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # db controlWebPage
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from controlWebPage import routes