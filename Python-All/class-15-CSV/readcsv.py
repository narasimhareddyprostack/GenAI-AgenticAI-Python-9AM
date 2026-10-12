import csv 

fp=open("emp.csv",'r')
emp_data=csv.reader(fp)
employees=list(emp_data)

#To remove CSV Header - using list slicing
for emp in employees[1:]:
    #print(emp)
    print(emp[1])

fp.close()