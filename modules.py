from view import db, datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	# image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	# posts = db.relationship('Post', backref='author', lazy=True)
	# usertype = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		# return f"User('{self.username}', '{self.email}', '{self.image_file}')"
		return f"User('{self.username}', '{self.email}')"

# user_1 = User(username='A_RIF_in', email='A_RIF_in@gmail.com', password='rif12345lolo')
# user_2 = User(username='U_RIF_in', email='U_RIF_in@gmail.com', password='rifko156ko')

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.data_posted}')"