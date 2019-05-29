import psycopg2
import sys
import re

con = psycopg2.connect(
    host = 'localhost',
    database='Music',
    user='postgres',
    password='111111'
)

cursor = con.cursor()

def create_table():
    create_query = '''
    create table music (
    id SERIAL primary key,
    artist text,
    title text,
    status integer default 0
    ) '''
    cursor.execute(create_query)
    con.commit()

# create_table()

#print(sys.argv)
# if sys.argv[1] == 'a':
#     print(sys.argv)



def add_a_song():
    add_query = 'insert into music (artist, title) values (%s, %s)'
    r1 = re.compile(r'(.*)[:,]')
    r2 = re.compile(r'[:,]\s(.*)')
    artist = r1.match(sys.argv[2]).group(1)
    title = r2.search(sys.argv[2]).group(1)

    cursor.execute(add_query, (artist, title))
    con.commit()

print(len(sys.argv))
if sys.argv[1] == 'a' and len(sys.argv) == 3:
    add_a_song()
elif sys.argv[1] == 'a' and len(sys.argv) == 6:
    add_query = 'insert into music (artist, title) values (%s, %s)'
    cursor.execute(add_query, (sys.argv[3], sys.argv[5]))
    con.commit()


cursor.close()
con.close()






