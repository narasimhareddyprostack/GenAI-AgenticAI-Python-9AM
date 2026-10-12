import requests 
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
status_code=user_resp.status_code

print(status_code)
print(users)