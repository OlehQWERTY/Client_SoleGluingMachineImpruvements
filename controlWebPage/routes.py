from flask import render_template, url_for, flash, redirect, abort, Response
from flask import make_response, request
from flask import jsonify  # for ajax
from controlWebPage import app, db, bcrypt
from controlWebPage.forms import RegistrationForm, LoginForm
from controlWebPage.modules import User, Post
from flask_login import login_user
# --------------------------

from time import time
import random # random
# from datetime import datetime, timedelta  # cookie test
# import base64

posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}
]


tasks = [
	{
		'RecID': '1',
		'UnitID': '1',
		'Articul': 'Nasty',
		'ProcessID': '101',
		'ProcessIDsDescription': "101 - add, 102 - del in case of damage, 103 - calc error",
		'OperatorName': 'Zoya Semenovna',
		'OperationDate': '17/11/18:17-25-36',
		'Pull': '197mljfuy',
		'OrderNumber': '145878925loi',
		'LocalNumber': '12',
		'PartLocalNumber': '4',
		'ReadyDate': '18/11/18:25-30-36',
		'CountryOrder': 'PL',
		'CityOrder': 'Lublin',
		'PlantOrder': 'RIF - 5',
		'DateEntered': '18/12/19:25-25-36',
		'RequiredRDate': '17/11/18:17-0-0',
		'CountryProd': 'UK',
		'CityProd': 'Kyiv',
		'QR': '186547'
	},
	{
		'RecID': '1',
		'UnitID': '1',
		'Articul': 'Kate',
		'ProcessID': '101',
		'ProcessIDsDescription': "101 - add, 102 - del in case of damage, 103 - calc error",
		'OperatorName': 'Zoya Semenovna',
		'OperationDate': '17/11/18:17-25-42',
		'Pull': '199poi',
		'OrderNumber': '199987',
		'LocalNumber': '13',
		'PartLocalNumber': '1',
		'ReadyDate': '18/11/18:25-30-36',
		'CountryOrder': 'PL',
		'CityOrder': 'Lublin',
		'PlantOrder': 'RIF - 5',
		'DateEntered': '18/12/19:25-25-36',
		'RequiredRDate': '17/11/18:17-0-0',
		'CountryProd': 'UK',
		'CityProd': 'Kyiv',
		'QR': '186551'
	}
]

machines = [  # from machines config db
	{
		'1': 4,
		'2': 4,
		'3': 6,
		'4': 4,
		'5': 4,
		'6': 6,
		'7': 4,
		'8': 6
	}
]

mProgress = [  # test temp: before db'll be added
	{
		'1': [[400, 900], [400, 900], [400, 900], [410, 500]],
		'2': [[436, 1100], [15, 210], [125, 860], [400, 900]],
		'3': [[400, 900], [400, 900], [400, 900], [400, 900], [400, 900], [None, 125]],  # add None processing
		'4': [[400, 900], [400, 900], [None, 900], [400, ]],
		'5': [[100, 2000], [400, 900], [300, 900], [200, 900]],
		'6': [[400, 1000], [400, 900], [400, 1200], [400, 700], [400, 520], [600, 900]],
		'7': [[400, 1000], [120, 900], [400, 1200], [425, 900]],
		'8': [[400, 900], [400, 900], [560, 900], [400, 900], [400, 900], [400, 900]]
	}
]

flgLoading = False  # show loading div instead of content

iop = 1000
@app.route('/_add_mProgress')  # ajax test
def add_mProgress():

	return jsonify(result=[random.randint(0, 10), 1000 - iop])


@app.route('/_get_numbers')  # ajax test
def add_numbers():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	return jsonify(result=a + b)


@app.route('/')
def home():
	# if not request.script_root:
	# 	# this assumes that the 'index' view function handles the path '/'
	# 	request.script_root = url_for('home', _external=True)
	return render_template('main.html', flgLoading=flgLoading)
	# return 'Main, page!'


@app.route('/machine/<number>')
def machineP(number=None):
	if number and int(number) > 8:
		current_pos_ammount = None
	else:
		current_pos_ammount = machines[0][str(number)]

	return render_template('machine.html', flgLoading=flgLoading, number=number, machine=current_pos_ammount)  # , name=name , name="name" [0][number]# , name=name , name="name" [0][number]

@app.route('/machine/all')
def machineAll():
	return render_template('machineAll.html', flgLoading=flgLoading, machines=machines[0], mProgress=mProgress)


@app.route('/task/')
@app.route('/task/list')
# @app.route('/task/<name>')
def taskP():
	return render_template('task.html', flgLoading=flgLoading, tasks=tasks)  #  True if dict == dict1 else False


@app.route('/task/add')
def taskAddP():
	return render_template('taskAdd.html', flgLoading=flgLoading)  # , tasks=tasks


@app.route("/register", methods=['GET', 'POST'])
def register(): 
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You\'re able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', flgLoading=flgLoading, title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	global loggedIn
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
			# abort(401)
	return render_template('login.html', flgLoading=flgLoading, title='Login', form=form)


# @app.route('/set')
# def index():
# 	# resp = make_response('lol')  # render_template(...)
# 	resp = make_response(render_template('taskAdd.html'))  # render_template(...)	 ---- redirect to page ----
# 	expire_date = datetime.now()
# 	print(expire_date)
# 	expire_date = expire_date + timedelta(seconds = 1)  # days=90
# 	resp.set_cookie('userID', value='I am cookie')
# 	key = 'u1'
# 	guid = 'lo'
# 	resp.set_cookie(key, guid, expires=expire_date) # expires=0 expires=expire_date
# 	resp.set_cookie(key, guid, expires=0) # expires 0 (unix time == 0 and dell imidiatelly)
# 	return resp 


# user ????
# @app.route('/del')
# def index1():
# 	# resp = make_response('lol')  # render_template(...)
# 	resp = make_response(render_template('taskAdd.html'))  # render_template(...)	 ---- redirect to page ----
# 	resp.delete_cookie('username', path='/', domain='0.0.0.0')
# 	# return '<h1>welcome</h1>'
# 	return resp 

# @app.route('/get')
# def getcookie():
# 	name = request.cookies.get('userID')
# 	test = request.cookies.get('u1')
# 	return '<h1>welcome '+ str(name) + ' ' + str(test) +'</h1>'