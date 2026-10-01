import random

enames=["Arunima","Gowri","Neeshanth","Ravi","Chandan","Sreenath","Ankit"]

lucky_dip_names=random.choices(enames,k=3)
print(lucky_dip_names)