import psycopg2
import json
import csv
import xml.etree.ElementTree as ET

con = psycopg2.connect(
    host = 'localhost',
    database='Employee',
    user='postgres',
    password='111111'
)

cursor = con.cursor()

#create table
def create_table():
    create_query = '''CREATE TABLE employee (
        id SERIAL primary key,
        first_name text,
        last_name text,
        birth_date date,
        gender text,
        monthly_salary float
    )'''
    cursor.execute(create_query)
    con.commit()



#read csv files
def read_csv(file):
    with open (file, 'r') as f:
        employees_list = csv.DictReader(f)
        employees = []
        for employee in employees_list:
            employees.append(employee)
        return employees

#read json files
def read_json(file):
    with open (file, 'r') as f:
        employees = json.load(f)
        for employee in employees:
            employee['first_name'] = employee['name'].split(' ')[0]
            employee['last_name'] = employee['name'].split(' ')[1]
            
        return employees

#read xml files
def read_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    children = list(root)
    employees = []
    for child in children:
        row = {}
        for element in child:
            if element.tag == 'salary_by_year':
                row['monthly_salary'] = float(element.text)/12
            if element.tag == 'name':
                row['first_name'] = element.text.split(' ')[0]
                row['last_name'] = element.text.split(' ')[1]
            else:
                row[element.tag] = element.text
        employees.append(row)
    return employees

        
#insert employees
def insert_employees(employees):
    insert_query = "insert into employee (first_name, last_name, birth_date, gender, monthly_salary) values (%s, %s, %s, %s, %s)"
    for employee in employees:

        cursor.execute(insert_query, (employee['first_name'],employee['last_name'], employee['birth_date'], employee['gender'], employee['monthly_salary']))
    con.commit()

#create_table()
# csv_employees = read_csv('employees.csv')
# insert_employees(csv_employees)

# json_employees = read_json('employees.json')
# insert_employees(json_employees)

# xml_employees = read_xml('employees.xml')
# insert_employees(xml_employees)



#Which first name is the most common in the company?

query1 = "SELECT COUNT(first_name) as count, first_name from employee group by first_name ORDER BY count DESC LIMIT 1"
cursor.execute(query1)
print(f'the most common first name is: {cursor.fetchall()}')


#Which first name is the most common among the younger (<30) employees?
query2 = '''SELECT COUNT(first_name) as count, first_name from employee
where (current_date - birth_date)/365 <= 30
group by first_name 
ORDER BY count DESC 
LIMIT 1
'''
cursor.execute(query2)
print(f'the most common first name among the younger is: {cursor.fetchall()}')



#What is the median salary in the company?

query3 = '''
SELECT emp.monthly_salary FROM
(
    SELECT e1.id, e1.monthly_salary, COUNT(e2.monthly_salary) salary_rank
    from employee e1, employee e2
    where e1.monthly_salary < e2.monthly_salary or (e1.monthly_salary = e2.monthly_salary and e1.id = e2.id)
    group by e1.id, e1.monthly_salary
    order by e1.monthly_salary DESC, e1.id DESC
) as emp 
where emp.salary_rank=(select count(*)/2 from employee)
 '''
cursor.execute(query3)
print(f'the median salary is: {cursor.fetchall()}')


#How many employee earns more than the average? 
query4 = '''
select count(*) from employee 
where monthly_salary >
(select AVG(monthly_salary) from employee)
 '''
cursor.execute(query4)
print(f'how many people earns more than the average: {cursor.fetchall()}')

#Increase the salary by monthly $100 for everybody who earns less than the median

query5 = '''
update employee set monthly_salary = monthly_salary + 100 
where monthly_salary < (
  SELECT emp.monthly_salary FROM
(
    SELECT e1.id, e1.monthly_salary, COUNT(e2.monthly_salary) salary_rank
    from employee e1, employee e2
    where e1.monthly_salary < e2.monthly_salary or (e1.monthly_salary = e2.monthly_salary and e1.id = e2.id)
    group by e1.id, e1.monthly_salary
    order by e1.monthly_salary DESC, e1.id DESC
) as emp 
where emp.salary_rank=(select count(*)/2 from employee)  
)
 '''
cursor.execute(query5)

cursor.close()
con.close()





