import csv 
employee_data=[
               [101,'Rahul',45000],
               [102,'Sonia',55000],
               [103,'Priya',65000]
              ]
fp=open('user.csv','w',newline="")
csv_wr=csv.writer(fp)

#creating csv header
csv_wr.writerow(['uid','uname','salary'])  

# Write data into csv file
csv_wr.writerows(employee_data)

print("New file Created successfully")
fp.close()