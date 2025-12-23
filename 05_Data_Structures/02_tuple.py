tup = (10,20,30,60,70,92,43,123,234,45,3,32)

print(tup)
print(tup[2])
# tup[2] = 5  throws error

tup_3 = (10,20,30) #tuple unpacking
a,b,c = tup_3
print(a)
print(b)
print(c)

print(tup.count(10))
print(tup.index(3))
