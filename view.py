from app import app
from flask import render_template

# @app.route("/hello")
# def hello():
# 	return "Hello World!"
@app.route('/')
def h_main():
	return 'Main, page!'

@app.route('/machines/')
@app.route('/hello1/<name>')
def hello1(name=None):
	# name = "name"
	return render_template('index.html', name=name)  # , name="name"