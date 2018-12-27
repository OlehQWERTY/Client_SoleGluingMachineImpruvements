# $ pip install Flask
# $ FLASK_APP=client.py flask run
#  * Running on http://localhost:5000/

from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"
@app.route('/')
def h_main():
    return 'Main, page!'

@app.route('/hello1/')
@app.route('/hello1/<name>')
def hello1(name=None):
    return render_template('index.html', name=name)