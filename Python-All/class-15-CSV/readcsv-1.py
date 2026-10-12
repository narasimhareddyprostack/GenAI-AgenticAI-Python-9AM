import csv 

fp=open("emp.csv",'r')
emp_data=csv.reader(fp)
print(type(emp_data))
employees=list(emp_data)
print(employees)
fp.close()