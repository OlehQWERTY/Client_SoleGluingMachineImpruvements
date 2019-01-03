from app import app
# from flask import render_template

from flask import Flask, render_template, url_for, flash, redirect, abort, Response
from forms import RegistrationForm, LoginForm

from time import time

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
		'1': [1, 40],'1': [2, 40],'1': [3, 40],'1': [4, 40],
		'2': [1, 50],'2': [2, 50],'2': [3, 50],'2': [4, 50],
		'3': [1, 68],'3': [2, 68],'3': [3, 68],'3': [4, 68],'3': [5, 68],'3': [6, 68],
		'4': [1, 90],'4': [2, 90],'4': [3, 90],'4': [4, 90],
		'5': [1, 80],'5': [2, 80],'5': [3, 80],'5': [4, 80],
		'6': [1, 46],'6': [2, 46],'6': [3, 46],'6': [4, 46],'6': [5, 46],'6': [6, 46],
		'7': [1, 10],'7': [2, 10],'7': [3, 10],'7': [4, 10],
		'8': [1, 100],'8': [2, 100],'8': [3, 100],'8': [4, 100],'8': [5, 100],'8': [6, 100]
	}
]

@app.route('/')
def home():
	return render_template('main.html')
	# return 'Main, page!'


# @app.route('/machine/')
@app.route('/machine/<number>')
def machineP(number=None):
	if number and int(number) > 8:
		current_pos_ammount = None
	else:
		current_pos_ammount = machines[0][str(number)]

	return render_template('machine.html', number=number, machine=current_pos_ammount)  # , name=name , name="name" [0][number]# , name=name , name="name" [0][number]

@app.route('/machine/all')
def machineAll():
	return render_template('machineAll.html', machines=machines[0], mProgress=mProgress)


@app.route('/task/')
@app.route('/task/list')
# @app.route('/task/<name>')
def taskP():
	return render_template('task.html', tasks=tasks)  # , name=name , name="name"


@app.route('/task/add')
def taskAddP():
	return render_template('taskAdd.html', tasks=tasks)  # , name=name , name="name" , title="LOL"


@app.route("/register", methods=['GET', 'POST'])
def register(): 
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	global loggedIn
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@controller.com' and form.password.data == '1234':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
			# abort(401)
	return render_template('login.html', title='Login', form=form)