from controlWebPage import db, login_manager
from datetime import datetime
# from view import db, datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	# image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	# posts = db.relationship('Post', backref='author', lazy=True)
	usertype = db.Column(db.String(20), nullable=False)
	createdby = db.Column(db.String(20), nullable=False)
	data_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	log = db.relationship('Log', backref='user', lazy=True)  # connected to Log table

	def __repr__(self):
		# return f"User('{self.username}', '{self.email}', '{self.image_file}')"
		return f"User('{self.username}', '{self.email}', '{self.usertype}')"

class Log(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	action_type = db.Column(db.String(20), nullable=False)
	action = db.Column(db.String(20), nullable=False)
	date_performed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	# add parameters(operators) saving ???
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # , nullable=False
	# user_email = db.Column(db.String(120), db.ForeignKey('user.email'))  # db.ForeignKey('user.email') , nullable=False ... in case of delating users user_id isn't valid 
	def __repr__(self):
		return f"Log('{self.action_type}', '{self.action}', '{self.date_performed}', '{self.user_id}')"  # , '{self.user_email}'
		
# no need now
# class Two(db.Model):
#     __bind_key__ = 'two'
#     id = db.Column(db.Integer, primary_key=True)
#     numb = db.Column(db.Integer)

# class Three(db.Model):
#     __bind_key__ = 'three'
#     id = db.Column(db.Integer, primary_key=True)
#     numb = db.Column(db.Integer)

#     CREATE TABLE glueMachine (
#     RecID int auto_increment primary key,
#     UnitID varchar(255),
#     Articul varchar(255),
#     ProcessID varchar(255),
#     ProcessIDsDescription varchar(255),
#     OperatorName varchar(255),
#     OperationDate varchar(255),
#     Pull varchar(255),
#     OrderNumber varchar(255),
#     LocalNumber varchar(255),
#     PartLocalNumber varchar(255),
#     ReadyDate varchar(255),
#     CountryOrder varchar(255),
#     CityOrder varchar(255),
#     PlantOrder varchar(255),
#     DateEntered varchar(255),
#     RequiredRDate varchar(255),
#     CountryProd varchar(255),
#     CityProd varchar(255),
#     QR varchar(255),
#     Extended_1 varchar(255),
#     Extended_2 varchar(255),
#     Extended_3 varchar(255),
#     Extended_4 varchar(255),
#     Extended_5 varchar(255),
#     Extended_6 varchar(255),
#     Extended_7 varchar(255),
#     Extended_8 varchar(255),
#     Extended_9 varchar(255),
#     Extended_10 varchar(255),
#     Extended_12 varchar(255),
#     Extended_13 varchar(255),
#     Extended_14 varchar(255),
#     Extended_15 varchar(255),
#     Extended_16 varchar(255),
#     Extended_17 varchar(255),
#     Extended_18 varchar(255),
#     Extended_19 varchar(255),
#     Extended_20 int,
#     Extended_22 int,
#     Extended_23 int,
#     Extended_24 int,
#     Extended_25 int,
#     Extended_26 int,
#     Extended_27 int,
#     Extended_28 int,
#     Extended_29 int
# );