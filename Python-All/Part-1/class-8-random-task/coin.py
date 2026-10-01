import random 

coin_flip=["Head","Tail"]
hcount=0
tcount=0
for num in range(100):
    result=random.choice(coin_flip)
    if result=="Head":
        hcount+=1 
    elif result=="Tail":
        tcount+=1 

print("No of Head's Count:",hcount)
print("No of Tails's Count:",tcount)
