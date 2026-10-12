fp=open('user.txt','r')
#print all file pointer properties
print(fp.name)
print(fp.readable())
print(fp.writable())

print(fp.mode)
#verify file closed or not
print(fp.closed)

#close the file pointer
fp.close()
#verify file closed or not
print(fp.closed)