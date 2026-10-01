#generate 10 - 4 Digit random numbers

from random import randint

i=0
while i<10:
    print(randint(1000,9999))
    i=i+1

""" 
for num in range(10):
    print(randint(1000,9999)) """