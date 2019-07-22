mylist = [1,2,3,4,5,6]

for i in range(len(mylist)-1,0,-1):
    print(mylist[i])
    if i==-1:
        break
else:
    print("sssssss")

# reversed(mylist)
mylist.reverse()
print(mylist)
# print(list(reversed(mylist)))

mylist[2],mylist[3] = mylist[3],mylist[2]
print(mylist)

aa = mylist[4:5]
aa[4],aa[5]