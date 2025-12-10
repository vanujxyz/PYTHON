a = 10
b = 10
c = 20
d = 30
# arithmetic
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a/b = {a/b}")
print(f"a%b = {a%b}")
print(f"a**b = {a**b}")
print(f"d//c = {d//c}")

# comparison

print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# logical
print(a == b and b == c)
print(a == b or b == c)
print(not(b>c))

# assignment
a += 10
a -= 10
a *= 10
a /= 10

#membership
x = ['apple','mango','banana']
print('banana' in x)
print('apple' not in x)

#identity
print(a) #here initially is not is true because the value is a float after division
print(int(a) is b)
print(b is not a)