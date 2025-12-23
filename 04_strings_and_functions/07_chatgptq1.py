sentence = input()
ls = sentence.split()
d = {}
for i in set(ls):
    count = 0
    for j in ls:
        if i == j :
            count += 1
    d[i] = count
print(d)