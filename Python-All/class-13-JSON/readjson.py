import json 

fp=open('emp.json','r')
employees=json.load(fp)

print(len(employees))
print(type(employees))

for emp in employees:
    print(emp['ename'])