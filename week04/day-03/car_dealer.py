import psycopg2
import json

con = psycopg2.connect(
    host = 'localhost',
    database='Car',
    user='postgres',
    password='111111'
)

cursor = con.cursor()

# create_table_query = 'CREATE TABLE cars (
#     id SERIAL primary key, 
#     brand text,
#     model text,
#     year integer,
#     condition text,
#     price integer,
#     count integer
# )'
f = open('cars.json','r')
cars = json.load(f)

def load_data(car):
    insert_query = "INSERT INTO cars VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (car['id'], car['brand'], car['model'], car['year'], car['condition'], car['price'], car['count']))


con.commit()

def remove_cars_not_on_stock():
    remove_query = 'DELETE FROM cars WHERE count = 0'
    cursor.execute(remove_query)
    con.commit()

#remove_cars_not_on_stock()

def decrease_price():
    update_query = "UPDATE cars SET price = (price * 0.8) WHERE condition = 'wreck' "
    cursor.execute(update_query)
    con.commit()

#decrease_price()

def count_avg_age():
    select_query = "SELECT AVG(2019-year) FROM cars WHERE count<> 0"
    cursor.execute(select_query)
    avg_age = cursor.fetchall()
    return avg_age


cursor.close()
con.close()






