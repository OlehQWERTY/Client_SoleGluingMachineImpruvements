from app import app
from flask import render_template

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
def mainP():
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
	return render_template('taskAdd.html', tasks=tasks)  # , name=name , name="name"
