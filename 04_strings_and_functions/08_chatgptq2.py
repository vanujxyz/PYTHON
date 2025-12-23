name = input("enter name: ")

marks = []
for i in range(3):
    marks.append(int(input(f"enter marks {i+1} : ")))

d = {}
d[name] = marks

total = 0
for i in d[name]:
    total += i

avg = total / 3

print(f"marks = {tuple(d[name])}")
print(f"max marks = {max(d[name])}")
print(f"avg marks = {avg}")
