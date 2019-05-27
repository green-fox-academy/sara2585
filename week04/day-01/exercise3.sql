--Create the necessary tables and maybe add the necessary fields
create table employees(
id int,
First_name text,
Last_name text,
Username text,
Date_of_employment DATE,
Date_of_exit DATE,
Role text,
Salary integer)


--Alter the existing tables so that an employee belongs to a department as well
ALTER table employees add Department text;


--Remove the username field from the table
alter table employees
drop username;

--Rename a column
alter table employees
RENAME id to user_id;