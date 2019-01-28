from flask import render_template, url_for, flash, redirect, abort, Response
from flask import make_response, request
from flask import jsonify  # for ajax
from controlWebPage import app, db, bcrypt, mSql, mydb, mycursor
from controlWebPage.forms import RegistrationForm, LoginForm, TaskAddForm, MachineForm
from controlWebPage.modules import User, Log
from flask_login import login_user, current_user, logout_user, login_required
# --------------------------
from time import time
import random # random
from datetime import datetime, timedelta  # cookie test
# import base64
# from time import sleep


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
@login_required
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
@login_required
def machineP(number=None):
	if number and int(number) > 8:
		current_pos_ammount = None
	else:
		current_pos_ammount = machines[0][str(number)]


	form = MachineForm()
	if form.is_submitted():

		print(form.operatorsName.data)  # не виводить якогось дива

		query = {
			'OperatorsName': form.operatorsName.data,
			'OperatorsSecondname': form.operatorsSecondname.data,
			'WorkingChange': form.workingChange.data,
			'CityProduction': form.cityProduction.data,
			'stateProduction': form.stateProduction.data,
			'PlantOrder': form.plantOrder.data,
			'CityProduction': form.cityProduction.data,
			'StateProduction': form.stateProduction.data,
			'PlantProduction': form.plantProduction.data,
			'Bunch': form.bunch.data,
			'Pull': form.pull.data,
			'localNumber': form.localNumber.data,
			'SQL_Table_NAME_': 'Config'
		}

		# insertSole_1(**query)
		print(getRecsSole_1("MachineID, Pos_1", "Config"))

	return render_template('machine.html', flgLoading=flgLoading, form=form, number=number, machine=current_pos_ammount)  # , name=name , name="name" [0][number]# , name=name , name="name" [0][number]
	# return render_template('machine.html', flgLoading=flgLoading, number=number, machine=current_pos_ammount)  # , name=name , name="name" [0][number]# , name=name , name="name" [0][number]


@app.route('/machine/all')  # with ajax
@login_required
def machineAll():
	# setCookie('test', 'val')  # save cookies
	# print(getCookie('test'))
	# delCookie('u1')
	# delCookie('userID')

	return render_template('machineAll.html', flgLoading=flgLoading, machines=machines[0], mProgress=mProgress)


@app.route('/task/')
@app.route('/task/list')
# @app.route('/task/<name>')
@login_required
def taskP():
	taskTable = getRecsSole_1("Bunch, Pull, LocalNumber, DateRequired, StateProduction, StateProduction", "Tasks")  # get tasks from db
	return render_template('task.html', flgLoading=flgLoading, tasks_list=taskTable)  #  True if dict == dict1 else False


@app.route('/task/add', methods=['GET', 'POST'])
@login_required
def taskAddP():
	# global flgLoading  # crutch: change it --------- !
	# flgLoading = False
	# print(flgLoading)

	form = TaskAddForm()
	# print("validation")
	# print(form.is_submitted())
	# print(form.validate_on_submit())
	if form.is_submitted():

		# print(form.dateRequired.data)

		query = {
			'Bunch': form.bunch.data,
			'Pull': form.pull.data,
			'LocalNumber': form.localNumber.data,
			'CityOrder': form.cityOrder.data,
			'StateOrder': form.stateOrder.data,
			'PlantOrder': form.plantOrder.data,
			'CityProduction': form.cityProduction.data,
			'StateProduction': form.stateProduction.data,
			'PlantProduction': form.plantProduction.data,
			'DateEnteredTask': form.dateEnteredTask.data,
			'DateEnteredToProduction': form.dateEnteredToProduction.data,
			'DateRequired': form.dateRequired.data,
			'SQL_Table_NAME_': 'Tasks'
		}

		# don't turn on commit 1/24/2019 @ 1:13 PM bug "display:block;" for content section (in taskAdd tamplate)
		# global flgLoading  # temp crutch
		# flgLoading = True
		insertSole_1(**query)
		# flgLoading = False

	return render_template('taskAdd.html', flgLoading=flgLoading, form=form)  # , tasks=tasks


@app.route("/register", methods=['GET', 'POST'])
@login_required  # only admin can create new users
def register(): 
# 	if current_user.is_authenticated:  # ordinary logic already login user can't register
# 		return redirect(url_for('home'))

	# in this prj only autentificated user with usertype=='admin' is able to add new users
	if not current_user.is_authenticated:
		return redirect(url_for('home'))
	elif current_user.usertype != 'admin':
		return redirect(url_for('home'))

	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		utype = 'admin' if form.usertype.data else 'user'
		user = User(username=form.username.data, email=form.email.data, password=hashed_password, usertype=utype, createdby=current_user.username)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You\'re able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', flgLoading=flgLoading, title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			log("authentication", "login", "successful", current_user.id)
			next_page = request.args.get('next')
			# redirect to page that you've visited just before you were redirected to log page
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
			log("authentication", "login", "unsuccessful")
			# abort(401)
			# utype=current_user.usertype - show register for admin user
	return render_template('login.html', flgLoading=flgLoading, title='Login', form=form) 


@app.route("/logout")
def logout():
	log("authentication", "logout", 'None', current_user.id)
	logout_user()
	return redirect(url_for('home'))


@app.route("/account")
@app.route("/account/<command>")
@login_required
def account(command=None):
	if command == '+clearAll':
		logClear(100000)
	elif command == '+clear3d':
		logClear(3)

	print(command)

	logTable = getLogTable()
	userTable = getUserTable()
	return render_template('account.html', title='Account', utype=current_user.usertype, logTable=logTable, userTable=userTable)


def log(a_type, act, cont, u_id = None):
	if u_id:
		db.session.add(Log(action_type=a_type, action=act, content=cont, user_id=u_id))
	else:
		db.session.add(Log(action_type=a_type, action=act, content=cont))
	db.session.commit()


def logClear(days_ago):  # days_ago
	days_ago = 3
	Log.query.filter(Log.date_performed > (datetime.now() - timedelta(days=days_ago))).delete()
	db.session.commit()


def getLogTable():
	return Log.query.all()


def getUserTable():
	return User.query.all()


def getSole_1():
	mycursor.execute("SELECT UnitID, Articul, ProcessID, OperatorName, OperationDate, Pull, OrderNumber, LocalNumber, ReadyDate FROM glueMachine")
	return mycursor


def insertSole_1(**data):
	if data['SQL_Table_NAME_'] == "glueMachine":  # is not used
	# Error with bracets 'data['UnitID']'
		query = "INSERT INTO " + str(data['SQL_Table_NAME_']) + " (UnitID, Articul, ProcessID, OperatorName, OperationDate, \
		Pull, OrderNumber, LocalNumber, ReadyDate) VALUES (" \
		+ data['UnitID'] + ', '  + '\'' + str(data['Articul']) + \
		'\'' + ', ' + data['ProcessID'] + ', ' + '\'' + str(data['OperatorName']) + '\'' + ', ' + '\'' + \
		str(data['OperationDate']) + '\'' + ', ' + '\'' + str(data['Pull']) + '\'' + ', ' + '\'' + \
		str(data['OrderNumber']) + '\'' + ', ' + '\'' + str(data['LocalNumber']) + '\'' + ', ' + '\'' + \
		str(data['ReadyDate'])  + '\'' + ')'

	elif data['SQL_Table_NAME_'] == "Tasks":
		query = "INSERT INTO " + str(data['SQL_Table_NAME_']) + " (Bunch, Pull, LocalNumber, CityOrder, StateOrder,	PlantOrder, CityProduction, \
		StateProduction, PlantProduction, DateEnteredTask, DateEnteredToProduction, DateRequired) VALUES (" \
		+ '\'' + str(data['Bunch']) + '\'' + ', '  + '\'' + str(data['Pull']) + \
		'\'' + ', ' + str(data['LocalNumber']) + ', ' + '\'' + str(data['CityOrder']) + '\'' + ', ' + '\'' + \
		str(data['StateOrder']) + '\'' + ', ' + '\'' + str(data['PlantOrder']) + '\'' + ', ' + '\'' + \
		str(data['CityProduction']) + '\'' + ', ' + '\'' + str(data['StateProduction']) + '\'' + ', ' + '\'' + \
		str(data['PlantProduction'])  + '\'' + ', ' + '\'' + str(data['DateEnteredTask']) + '\'' + ', ' + '\'' + \
		str(data['DateEnteredToProduction']) + '\'' + ', ' + '\'' + str(data['DateRequired']) + '\'' + ')'
	elif data['SQL_Table_NAME_'] == "Config":  # continue point
		query = "INSERT INTO " + str(data['SQL_Table_NAME_']) + " (Bunch, Pull, LocalNumber, CityOrder, StateOrder,	PlantOrder, CityProduction, \
		StateProduction, PlantProduction, DateEnteredTask, DateEnteredToProduction, DateRequired) VALUES (" \
		+ '\'' + str(data['Bunch']) + '\'' + ', '  + '\'' + str(data['Pull']) + \
		'\'' + ', ' + str(data['LocalNumber']) + ', ' + '\'' + str(data['CityOrder']) + '\'' + ', ' + '\'' + \
		str(data['StateOrder']) + '\'' + ', ' + '\'' + str(data['PlantOrder']) + '\'' + ', ' + '\'' + \
		str(data['CityProduction']) + '\'' + ', ' + '\'' + str(data['StateProduction']) + '\'' + ', ' + '\'' + \
		str(data['PlantProduction'])  + '\'' + ', ' + '\'' + str(data['DateEnteredTask']) + '\'' + ', ' + '\'' + \
		str(data['DateEnteredToProduction']) + '\'' + ', ' + '\'' + str(data['DateRequired']) + '\'' + ')'
	else:
		prrint("Table is incorect or data is empty!")
		return False
	print(query)
	# print("Data: !!!")
	# print(query)
	try:
		mycursor.execute(query)
		mydb.commit()
	except mSql.Error as err:
		print("Failed inserting to database: {}".format(err))
		return False

	return True


def getRecsSole_1(fields, tableName):
	db_response = []
	query = "SELECT " + fields + " FROM " + tableName # + " WHERE RecID = " + str(id)
	print(query)
	try:
		mycursor.execute(query)
		mydb.commit()
	except mSql.Error as err:
		print("Failed getting from database: {}".format(err))
		return False

	for x in mycursor:
		db_response.append(x)

	print(db_response)
	return db_response


def delRecIDSole_1(id, id_2=None):
	try:
		mycursor.execute("SELECT COUNT(1) FROM glueMachine WHERE RecID = " + str(id))
		for x in mycursor:
			if id_2:  # del RecID in range(id, id_2). Unsafe because it doesn't include check procedure.
				query_2 = "DELETE FROM glueMachine WHERE RecID BETWEEN " + str(id) + " AND " + str(id_2)
				mycursor.execute(query_2)
				print("id = " + str(id) + '-' + str(id_2) + " should be delated")
				mydb.commit()
			else:  # del one RecID[id]
				query_1 = "DELETE FROM glueMachine WHERE RecID=" + str(id)
				if False if int(x[0]) > 0 else True:
					print("id = " + str(id) + " doesn't exist!")
					return False  # do not exist
				else:
					mycursor.execute(query_1)
					print("id = " + str(id) + " was del")
					mydb.commit()
	except mSql.Error as err:
		print("Failed deleting from database: {}".format(err))
	else:
		return True

# @app.route("/setCookie")

# NOT TESTED
# make_response( cheak string and so on
def setCookie(name, val, who_call):  # name, val
	# name, val = ['lolo', 'koko']
	# resp = make_response('lol')  # render_template(...)
	resp = make_response("render_template('" + who_call + "')")  # render_template(base.html)	 ---- redirect to page ----
	expire_date = datetime.now()
	print(expire_date)
	expire_date = expire_date + timedelta(days=4)  # seconds = 1 days=90
	print(expire_date)
	resp.set_cookie(name, value=val, expires=expire_date)
	# resp.set_cookie('language', value='I am cookie', expires=expire_date)
	# key = 'u1'
	# guid = 'lo'
	# resp.set_cookie(key, guid, expires=expire_date) # expires=0 expires=expire_date
	# resp.set_cookie(key, guid, expires=0) # expires 0 (unix time == 0 and dell imidiatelly)
	# return resp
	return redirect(url_for(who_call))

def delCookie(name): 
	resp = make_response("")
	resp.set_cookie(name, 'del_me', expires=0)

def getCookie(name):
	val = request.cookies.get(name)
	return val

# user ????
# @app.route('/del')
# def index1():
# 	# resp = make_response('lol')  # render_template(...)
# 	resp = make_response(render_template('taskAdd.html'))  # render_template(...)	 ---- redirect to page ----
# 	resp.delete_cookie('username', path='/', domain='0.0.0.0')
# 	# return '<h1>welcome</h1>'
# 	return resp 

@app.route('/get')
def getcookie():
	name = request.cookies.get('userID')
	test = request.cookies.get('u1')
	return '<h1>welcome '+ str(name) + ' ' + str(test) +'</h1>'