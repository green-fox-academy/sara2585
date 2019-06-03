import json
import re
from datetime import datetime
from collections import namedtuple
from functools import reduce


def read_json(file):
    with open (file, 'r') as f:
        histories = json.load(f)
        return histories

histories = read_json('gfa-team-thanks.json')


def get_histories_with_users(histories):
    histories_with_users = list(filter(lambda history: 'user' in history, histories))
    return histories_with_users



def get_history_with_message(histories):
    return list(filter(lambda history: 'client_msg_id' in history, histories))

Message = namedtuple('Message', 'id user_id message sent_at')

def get_messages(histories):
    histories1 = get_histories_with_users(histories)
    new_histories = get_history_with_message(histories1)
    return list(map(lambda history: Message(id= history['client_msg_id'], user_id=history['user'], message = history['text'], sent_at = datetime.fromtimestamp(int(history['ts'].split('.')[0]))), new_histories))

Mention = namedtuple('Mention', 'message_id user_id')

def find_all_mentioned_users(history):
    r = re.compile('<@(\w{9})>')
    users = r.findall(history['text'])
    return users


def get_mention_by_a_history(history):
    users = find_all_mentioned_users(history)
    return list(map(lambda user: Mention(message_id= history['client_msg_id'], user_id= user), users))


def get_mentions(histories):
    histories1 = get_histories_with_users(histories)
    new_histories = get_history_with_message(histories1) 
    mentions = list(map(lambda history: get_mention_by_a_history(history), new_histories))
    return list(reduce(lambda x, y: x+y, mentions))
    
    # print(mentions)


Reaction = namedtuple('Reaction', 'user_id message_id reaction')

def get_history_with_reaction(histories):
    histories_with_reaction = list(filter(lambda history: 'reactions' in history, histories))
    return histories_with_reaction

def get_reactions_by_a_history(history):
    reactions = history['reactions']
    return list(map(lambda reaction: get_reactions_by_a_reaction(reaction, history), reactions))


def get_reactions_by_a_reaction(reaction, history):
    users = reaction['users']
    return list(map(lambda user: Reaction(user_id= user, message_id= history['client_msg_id'], reaction= reaction['name']), users))
    

def get_reactions(histories):
    history_with_message = get_history_with_message(histories)
    history_with_reactions = get_history_with_reaction(history_with_message)
    mentions = list(map(lambda history: get_reactions_by_a_history(history), history_with_reactions))
    return list(reduce(lambda a, b: a+b ,list(reduce(lambda a, b: a+b, mentions))))


User = namedtuple('User', 'user_id')

def get_users(histories):
    histories_with_users = get_histories_with_users(histories)
    users = set()
    list(map(lambda history: users.add(history['user']), histories_with_users))
    return list(map(lambda user: User(user_id= user), users))



    






