unames=["RG","SG","PG","Modi"]
uids=(101,102,102,103,104)
eids={101,101,101,101,101}  #duplicats not allowed
ename="Rahul Gandhi"
b=bytes([10,20,30,255])
ba=bytearray([10,20,30,255])
fz=frozenset({10,10,10,10,10})
numbers=range(100)



print('RG' in unames)      #True

print(101 in eids)         #True
print(101 not in eids)     #False
print(102 not in eids)     #True

print('z' in ename)        #False

print("***checking in bytes and bytearray***")
print(20 in b)
print(20 in ba)
print(20 in fz)  #False