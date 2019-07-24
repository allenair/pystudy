mylist = [7,2,3,4,5,6]

mylist.sort()

print(mylist)

myset=set()
myset.add((1,2))
myset.add((1,3))
myset.add((1,2))

print(myset)

mytup = tuple(mylist)

print(mytup)

mylist = [list(x) for x in myset]
print(mylist)
