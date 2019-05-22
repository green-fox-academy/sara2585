from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"
    
@app.route('/myfirstwebsite')
def my_firstwebsite():
    return render_template('First website.html')