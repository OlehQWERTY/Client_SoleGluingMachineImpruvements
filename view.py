from app import app
from flask import render_template

# @app.route("/hello")
# def hello():
# 	return "Hello World!"
@app.route('/')
def mainP():
	return render_template('main.html')
	# return 'Main, page!'

@app.route('/machine/')
@app.route('/machine/<name>')
def machineP(name=None):  #name=None
	return render_template('machine.html', name=name)  # , name=name , name="name"

@app.route('/task/')
@app.route('/task/<name>')
def taskP(name=None):  #name=None
	return render_template('task.html', name=name)  # , name=name , name="name"