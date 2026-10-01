employees = [
	{"eid": 1001, "ename": "Aarav Sharma", "gender": "Male", "salary": 55000},
	{"eid": 1002, "ename": "Ananya Patel", "gender": "Female", "salary": 62000},
	{"eid": 1003, "ename": "Rohan Verma", "gender": "Male", "salary": 48000},
	{"eid": 1004, "ename": "Priya Singh", "gender": "Female", "salary": 71000},
	{"eid": 1005, "ename": "Vikram Reddy", "gender": "Male", "salary": 59000},
	{"eid": 1006, "ename": "Neha Gupta", "gender": "Female", "salary": 68000},
	{"eid": 1007, "ename": "Arjun Mehta", "gender": "Male", "salary": 53000},
	{"eid": 1008, "ename": "Sneha Iyer", "gender": "Female", "salary": 75000},
	{"eid": 1009, "ename": "Karan Malhotra", "gender": "Male", "salary": 61000},
	{"eid": 1010, "ename": "Meera Nair", "gender": "Female", "salary": 57000},
	{"eid": 1011, "ename": "Aditya Rao", "gender": "BiGender", "salary": 66000},
	{"eid": 1012, "ename": "Pooja Joshi", "gender": "Female", "salary": 52000},
	{"eid": 1013, "ename": "Rahul Kapoor", "gender": "Male", "salary": 73000},
	{"eid": 1014, "ename": "Kavya Das", "gender": "Female", "salary": 64000},
	{"eid": 1015, "ename": "Siddharth Bose", "gender": "Male", "salary": 58000},
	{"eid": 1016, "ename": "Ishita Roy", "gender": "Female", "salary": 69000},
	{"eid": 1017, "ename": "Manish Kumar", "gender": "Male", "salary": 50000},
	{"eid": 1018, "ename": "Riya Choudhary", "gender": "Female", "salary": 76000},
	{"eid": 1019, "ename": "Nikhil Jain", "gender": "Male", "salary": 63000},
	{"eid": 1020, "ename": "Simran Kaur", "gender": "Female", "salary": 60000},
]

mcount=0
fcount=0
for emp in employees:
    if emp['gender'] =="Male":
        mcount=mcount+1
    elif emp['gender']=="Female":
        fcount=fcount+1


print("No of Male Employees:",mcount)
print("No of Female Employees:",fcount)
