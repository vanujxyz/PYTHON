s = {11,1,33,54,67,23,34}
print(s,type(s))


s.add(1)
s.pop()
s.remove(33)
s.discard(500)
print(s)

a = {1,2,3,4,5}
b = {4,5,6,7,8,9}
c = {5,10,15,20,25,30}
print(a.union(b,c))
print(a.intersection(b,c))
print(b.difference(c))