import json 
emp={'eid': 101, 'ename': 'Rahul Gandhi', 'avail': True, 'loc': None}

emp_str=json.dumps(emp)
print(emp)
print(emp_str)
print(type(emp_str))