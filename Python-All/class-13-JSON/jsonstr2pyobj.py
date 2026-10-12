import json 
emp_str_json=""" 
                {
                "eid":101,
                "ename":"Rahul Gandhi",
                "avail":true,
                "loc":null
                }
                
             """

emp=json.loads(emp_str_json)
print(emp)