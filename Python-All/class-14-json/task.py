import json
fp=open('users.json','r')

users=json.load(fp)

print(type(users))
print(len(users))

for user in users:
    print(user['name'],":",user['address']['city'])