from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def hello_john():
    greetings = ['Hello,John!', 'Hi, John!', 'How are you today?']
    greeting = random.choice(greetings)
    return render_template('Greet_john.html', greeting = greeting)
