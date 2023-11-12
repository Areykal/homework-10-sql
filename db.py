import os
from dotenv import load_dotenv
import mysql.connector
from datetime import datetime

load_dotenv()

DB = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    db=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

cursor = DB.cursor()

'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''

# cursor.execute("SELECT * FROM employee")
# employees = cursor.fetchall()

# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'))

# date time conversion format
# https://www.w3schools.com/python/python_datetime.asp#:~:text=A%20reference%20of%20all%20the%20legal%20format%20codes%3A

# cursor.execute("SELECT * FROM employee WHERE emp_num > 101")
# employees_condition = cursor.fetchall()

# for employee in employees_condition:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'))

'''
Join employee with job and select emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate, job_description
'''

# cursor.execute("SELECT * FROM employee INNER JOIN job ON employee.job_code = job.job_code")
# employees = cursor.fetchall()
# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'), employee[9])

# OR

# cursor.execute('''SELECT 
#                em.emp_num, em.emp_lname, em.emp_fname, em.emp_initial, em.emp_hiredate, job.job_description  
#                FROM employee as em INNER JOIN job ON em.job_code = job.job_code''')

# employees = cursor.fetchall()
# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'), employee[5])

'''
Insert new employee record, emp_num = 999, emp_lname = Doe, emp_fname = John, emp_initial = D, emp_hiredate = current date
'''

# today = datetime.now()
# sql = 'INSERT INTO employee (emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate) VALUES (%s, %s, %s, %s, %s)'
# value = (168, 'Doe', 'John', 'JD', today)

# cursor.execute(sql, value)

# DB.commit()
# print(cursor.rowcount, "record inserted.")


'''
Update employee record, job_code = 510 where emp_num = 999
'''

# sql = """UPDATE employee
# SET job_code = %s
# WHERE emp_num = %s
# """
# values = (510, 999)

# cursor.execute(sql, values)

# employees = cursor.fetchall()

# DB.commit()

'''
Delete employee record, emp_num = 999
'''

# sql = """delete from employee
# where emp_num = %s
# """

# value = [(999)]
# cursor.execute(sql, value)
# DB.commit()

'''
Query assigment where assign_date is larger than 2010-01-01
'''

# sql = """Select * from assignment
# where assign_date > %s
# """

# value = ("2010-01-01",)

# cursor.execute(sql, value)

# assignments = cursor.fetchall()
# for assignment in assignments:
#     print(assignment)
    
# DB.commit()

"""
1. add new employee record to employee table with id = 168, firstname = 'John', 
lastname = 'Doe', initials = 'JD', job = 'Programmer', hire_date = today's date.
"""

# sql = """INSERT INTO employee (emp_num, emp_fname, emp_lname, emp_initial, job_code, emp_hiredate)
# VALUES (%s, %s, %s, %s, %s, %s)
# """
# current_date = datetime.now()

# values = (168, "John", "Doe", "JD", 500, current_date)

# cursor.execute(sql, values)
# DB.commit()

"""
2. query the new created employee (id=168) from employee table, with information of employee
id, firstname, lastname, initials, job description (join with job), charge per hour (join with
job) and hire_date.
"""

# sql = """
# select emp.emp_num, emp.emp_fname, emp.emp_lname, emp.emp_initial, job.job_description, job.job_chg_hour, emp.emp_hiredate
# from employee as emp
# join job using (job_code)
# where emp.emp_num = %s
# """
# value = (168,)

# cursor.execute(sql, value)
# new_employee = cursor.fetchall()

# print(new_employee)

"""
3. update the new created employee (id=168) job, from 'Programmer' to 'Database Designer'.
"""

# sql = """
# update employee
# set job_code = %s
# where emp_num = %s
# """

# values = (502, 168)

# cursor.execute(sql, values)
# DB.commit()

"""
4. query all project that has "Programmer" assigned to, with information of project id, 
project name and program manager (join with employee).
"""

# sql = """
# select proj.proj_num, proj.proj_name, emp.emp_fname, emp.emp_lname
# from project as proj
# join employee as emp using (emp_num)
# where emp.job_code = %s
# """

# value = (500,)

# cursor.execute(sql, value)
# programmers = cursor.fetchall()

# print(programmers)

"""
5. delete the new created employee (id=168) from employee table.
"""

# sql = """
# delete from employee 
# where emp_num = %s
# """

# value = (168,)

# cursor.execute(sql, value)

# DB.commit()