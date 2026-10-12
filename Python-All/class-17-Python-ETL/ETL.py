import requests,json,csv 
#Extract data from Rest API's/Databases/Files
Rest_API_URL='https://dummyjson.com/products'
prod_resp=requests.get(Rest_API_URL)
products=prod_resp.json()['products']
#Transofrm
product_json=[]
product_csv=[]
for prod in products:
    product_json.append({
        "pid":prod['id'],
        "name":prod['title'],
        "category":prod['category'],
        "rating":prod['rating']
    })
    product_csv.append((prod['id'],
                        prod['title'],
                        prod['category'],
                        prod['price'],
                        prod['rating'])
                        )

#print(product_json)
#Load into new JSON File and CSV File
fp1=open('New_Products.json','w')
fp2=open('New_Products.csv','w',newline='')
csv_wr=csv.writer(fp2)
#create CSV file Header
csv_wr.writerow(['pid','name','category','price','rating'])
csv_wr.writerows(product_csv)

json.dump(product_json,fp1)
print("New JSON File Created Successfully")
print("New CSV File Created Successfully")
