import csv
f=open('employee_data.csv','r')
file_reader=csv.reader(f)
next(file_reader)
no_of_high_employees=0
Total_salary_of_Employees=0
for i in file_reader:
    current_salary=int(i[2])
    if current_salary > 7000:
        no_of_high_employees+=1
    Total_salary_of_Employees+=current_salary
print(f'Total salary of employees = {Total_salary_of_Employees}')
print(f'Number of high employees = {no_of_high_employees}')


