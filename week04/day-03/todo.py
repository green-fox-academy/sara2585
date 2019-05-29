import psycopg2
import sys

con = psycopg2.connect(
    host = 'localhost',
    database='task',
    user='postgres',
    password='111111'
)

# print(con.get_dsn_parameters())

cursor = con.cursor()


def list_tasks():
    select_query = 'SELECT * FROM task ORDER BY id'
    cursor.execute(select_query)
    tasks = cursor.fetchall()
    return tasks
    

def add_task():
    insert_query = "INSERT INTO task (task) VALUES (%s)"
    cursor.execute(insert_query, (sys.argv[2],))
    con.commit()

def check_task():
    check_query = f'SELECT * FROM task Where id = {sys.argv[2]}'
    cursor.execute(check_query)
    task = cursor.fetchall()
    return task

def remove_task():
    delete_query = f'DELETE FROM task where id = {sys.argv[2]}'
    cursor.execute(delete_query)
    con.commit()

if sys.argv[1] == 'l':
    tasks = list_tasks()
    for task in tasks:
        print(f"{task[0]} - {task[1]}")

elif sys.argv[1] == 'a':
    add_task()

elif sys.argv[1] == 'c':
    task = check_task()
    print(f"{task[0][0]} - {task[0][1]}")

elif sys.argv[1] == 'r':
    remove_task()


cursor.close()
con.close()




