emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45
}
#update dict value
emp['ename']="Rahul Gandhi"

#delete - key:value pair
emp.pop('esal')
print(emp)