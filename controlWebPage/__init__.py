# template language: Jinja 2

from flask import Flask
from controlWebPage.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import mysql.connector

# some_engine = create_engine('mysql+mysqldb://monitor:password@172.16.2.142:3306/sole_1')
# python -m pip install mysql-connector


mydb = mysql.connector.connect(
  host="172.16.2.142",
  user="monitor",
  passwd="password",
  database="sole_1"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# print(mycursor)
# query = ("SELECT UnitID, Articul, ProcessID, OperatorName, OperationDate, Pull, OrderNumber, LocalNumber, ReadyDate FROM glueMachine")
# mycursor.execute(query)
mycursor.execute("SELECT UnitID, Articul, ProcessID, OperatorName, OperationDate, Pull, OrderNumber, LocalNumber, ReadyDate FROM glueMachine")

# mycursor.execute("USE sole_1")
# mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # db controlWebPage
# app.config['SQLALCHEMY_BINDS'] = {'two' : 'sqlite:///two.db', # no need now
#                                   'three' : 'sqlite:///three.db'}
db = SQLAlchemy(app)
# session_three = db.scoped_session(db.sessionmaker(bind=db.get_engine(app, 'three')))
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from controlWebPage import routes