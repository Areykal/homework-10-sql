1. add new employee record to employee table with id = 168, firstname = 'John',
   lastname = 'Doe', initials = 'JD', job = 'Programmer', hire_date = today's date.

sql = """

INSERT INTO employee (emp_num, emp_fname, emp_lname, emp_initial, job_code, emp_hiredate)

VALUES (%s, %s, %s, %s, %s, %s)

"""

current_date = datetime.now()

values = (168, "John", "Doe", "JD", 500, current_date)

cursor.execute(sql, values)

DB.commit()

2. query the new created employee (id=168) from employee table, with information of employee
   id, firstname, lastname, initials, job description (join with job), charge per hour (join with
   job) and hire_date.

sql = """

select emp.emp_num, emp.emp_fname, emp.emp_lname, emp.emp_initial, job.job_description, job.job_chg_hour, emp.emp_hiredate

from employee as emp

join job using (job_code)

where emp.emp_num = %s

"""

value = (168,)

cursor.execute(sql, value)

new_employee = cursor.fetchall()

print(new_employee)

3. update the new created employee (id=168) job, from 'Programmer' to 'Database Designer'.

sql = """

update employee

set job_code = %s

where emp_num = %s

"""

values = (502, 168)

cursor.execute(sql, values)

DB.commit()

4. query all project that has "Programmer" assigned to, with information of project id,
   project name and program manager (join with employee).

sql = """

select proj.proj_num, proj.proj_name, emp.emp_fname, emp.emp_lname

from project as proj

join employee as emp using (emp_num)

where emp.job_code = %s

"""

value = (500,)

cursor.execute(sql, value)

programmers = cursor.fetchall()

print(programmers)

5. delete the new created employee (id=168) from employee table.

sql = """

delete from employee

where emp_num = %s

"""

value = (168,)

cursor.execute(sql, value)

DB.commit()
