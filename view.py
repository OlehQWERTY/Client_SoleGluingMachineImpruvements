from app import app
from flask import render_template

# @app.route("/hello")
# def hello():
# 	return "Hello World!"
@app.route('/')
def h_main():
	return 'Main, page!'

@app.route('/machine/')
@app.route('/machie/<name>')
def machine(name=None):  #name=None
	# name = "name"
	return render_template('machine.html', name=name)  # , name=name , name="name"