import psycopg2


con = psycopg2.connect(
    host = 'localhost',
    database = 'slack',
    user = 'postgres',
    password = '111111'
)

cursor = con.cursor()

#Who reacted to the most messages?
views = ''' create view reacted_count as 
(select user_id, count(id) as reactions from reactions
group by user_id)'''


message_reactions = ''' create view message_reactions as 
(select m.id, count(r.id) as reactions, m.message  
 from messages m join reactions r 
 on m.id = r.message_id
group by m.id);'''


emoji_count = ''' create view emoji_count as 
(select reaction, count(id) as counts 
 from reactions group by reaction)'''


mentioned_by_others = '''create view mentioned_by_others as(
select distinct m1.user_id as user_id, count(distinct m2.id) as mentioned_uers
from mentions m1 join messages m2 on m1.message_id = m2.id
group by m1.user_id) '''


message_count_by_date  = '''create view messages_by_date as(

select  to_date(to_char(sent_at, 'YYYY/MM/DD'), 'YYYY/MM/DD') as date, count(id) 
from messages group by date
);
 '''

def create_view(query):
    cursor.execute(query)
    con.commit()



# cursor.execute(message_reactions)
# con.commit()

#Who reacted to the most messages?
def reacted_most_messages():
    select_query = 'select * from reacted_count order by reactions desc limit 5'
    cursor.execute(select_query)
    users = cursor.fetchall()
    return users

#Which message got the most reactions in the thanks channel?
def message_got_reactions():
    select_query = 'select * from message_reactions order by reactions desc limit 1'
    cursor.execute(select_query)
    messages = cursor.fetchall()
    return messages

#Which emoji is the most common as reaction in the thanks channel?
def most_common_emoji():
    select_query = 'select * from emoji_count order by counts desc limit 1'
    cursor.execute(select_query)
    emojis = cursor.fetchall()
    return emojis


#Who is the most active in the channel?
def most_active_employee():
    select_query = 'select * from message_count_by_users order by count desc limit 5'
    cursor.execute(select_query)
    active_users = cursor.fetchall()
    return active_users

#Which day sent the most messages?
def send_most_messages_date():
    select_query = 'select * from messages_by_date order by count desc limit 3'
    cursor.execute(select_query)
    messages_by_date = cursor.fetchall()
    return messages_by_date

# def send_most_messages_year():
#     select_query = ''
