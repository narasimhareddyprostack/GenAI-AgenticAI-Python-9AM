import requests

Rest_API_URL='https://dummyjson.com/products'
prod_resp=requests.get(Rest_API_URL)
products=prod_resp.json()['products']
print(len(products))