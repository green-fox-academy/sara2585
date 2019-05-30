from flask import Flask
from flask import render_template
from slack_methods import *


app = Flask(__name__)
    
@app.route('/home')
def home_page():
    return render_template('base.html')


@app.route('/reactions')
def get_reactions():
    emojis = most_common_emoji()
    return render_template('show_reaction_datas.html', emojis = emojis)


@app.route('/users')
def get_users():
    users = reacted_most_messages()
    active_users = most_active_employee()
    return render_template('show_user_datas.html', users = users, active_users = active_users)

@app.route('/messages')
def get_messages():
    messages = message_got_reactions()
    messages_by_date = send_most_messages_date()
    return render_template('show_message_datas.html', messages = messages, messages_by_date = messages_by_date)


    




    
    
    

