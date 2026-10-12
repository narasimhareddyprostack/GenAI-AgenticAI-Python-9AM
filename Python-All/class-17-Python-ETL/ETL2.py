import requests,json 
#Extract data from Rest API's/Databases/Files
Rest_API_URL='https://dummyjson.com/products'
prod_resp=requests.get(Rest_API_URL)
products=prod_resp.json()['products']
#Transofrm
product_json=[]
for prod in products:
    product_json.append({
        "pid":prod['id'],
        "name":prod['title'],
        "category":prod['category'],
        "rating":prod['rating']
    })

#print(product_json)
#Load into new JSON File and CSV File
fp=open('New_Product.json','w')
json.dump(product_json,fp)
print("New JSON File Created Successfully")