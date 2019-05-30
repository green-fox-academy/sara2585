import psycopg2
import json
import re
from datetime import datetime
con = psycopg2.connect(
    host = 'localhost',
    database = 'slack',
    user = 'postgres',
    password = '111111'
)

cursor = con.cursor()

def create_table(create_query):
    cursor.execute(create_query)
    con.commit()

table_users_query = '''create table users (
    id SERIAL primary key,
    user_id text,
    name text default null

) '''

#create_table(table_users_query)

table_messages_query = '''create table messages (
    id text primary key,
    user_id text,
    message text,
    channel text,
    sent_at timestamp
) '''



table_mentions_query = '''create table mentions (
    id SERIAL primary key,
    message_id text,
    user_id text

) '''
table_reactions_query = '''create table reactions (
    id SERIAL primary key,
    user_id text,
    message_id text,
    reaction varchar(128)

) '''



def read_json(file):
    with open (file, 'r') as f:
        histories = json.load(f)
        return histories




def insert_data_to_users(user):
    query = 'insert into users (user_id) values (%s)'
    cursor.execute(query, (user,))
    con.commit()

def insert_data_to_messages(history):
    query = 'insert into messages values(%s, %s, %s, %s, %s)'
    cursor.execute(query, (history['client_msg_id'], history['user'], history['text'], 'thanks channel', datetime.fromtimestamp(int(history['ts'].split('.')[0]))))
    con.commit()

def insert_data_to_mentions(history):
    query = 'insert into mentions (message_id, user_id) values(%s, %s)'
    r = re.compile('<@(\w{9})>')
    users = r.findall(history['text'])
    if users != []:
        for user in users:
            cursor.execute(query, (history['client_msg_id'], user))
    con.commit()


def insert_data_to_reactions(history):
    query = 'insert into reactions (user_id, message_id, reaction) values(%s, %s, %s)'
    if 'reactions' in history:
        reactions = history['reactions']
        for reaction in reactions:
            users = reaction['users']
            for user in users:
                    cursor.execute(query, (user, history['client_msg_id'], reaction['name']))

    con.commit()


def get_all_users(histories):
    users = set()
    for history in histories:
        if 'user' in history:
            users.add(history['user'])
            if 'reactions' in history:
                reactions = history['reactions']
                for reaction in reactions:
                    reaction_users = reaction['users']
                    for reaction_user in reaction_users:
                        users.add(reaction_user)
    return users


histories = read_json('gfa-team-thanks.json')

#insert_users
# users = get_all_users(histories)
# for user in users:
#     insert_data_to_users(user)

# for history in histories:
#     if 'client_msg_id' not in history:
#         print(history)


#create_table(table_messages_query)
#create mentions
#create_table(table_mentions_query)


# #create_reactions
# create_table(table_reactions_query)


#insert datas
# for history in histories:
#     if 'client_msg_id' in history:
#         insert_data_to_reactions(history)
#         insert_data_to_mentions(history)
#         insert_data_to_messages(history)












    
    










