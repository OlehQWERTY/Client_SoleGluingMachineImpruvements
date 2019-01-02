from app import app
# from flask import render_template

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

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

@app.route('/')
def home():
	return render_template('main.html')
	# return 'Main, page!'


@app.route('/machine/')
@app.route('/machine/<name>')
def machineP(name=None):  #name=None
	return render_template('machine.html', name=name)  # , name=name , name="name"


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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@controller.com' and form.password.data == '1234':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

