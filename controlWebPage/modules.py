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
	# log = db.relationship('Log', backref='user_name', lazy=True)  # connected to Log table

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
	# user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	# user_email = db.Column(db.String(120), db.ForeignKey('user.email'))  # db.ForeignKey('user.email') , nullable=False ... in case of delating users user_id isn't valid 
	def __repr__(self):
		return f"Log('{self.action}', '{self.date_performed}')"  # , '{self.user_email}'


# class Post(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String(20), nullable=False)
# 	data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
# 	content = db.Column(db.Text, nullable=False)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# 	def __repr__(self):
# 		return f"Post('{self.title}', '{self.data_posted}')"