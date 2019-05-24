from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def hello_john():
    greetings = ['Hello,', 'Hi, ', 'How are you today?']
    names = ['john', 'lucy', 'david']
    greeting = random.choice(greetings)
    name = random.choice(names)
    return render_template('Greet_John2.html', greeting = greeting, name = name)
