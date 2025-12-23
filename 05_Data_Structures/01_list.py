marks = [10,20,30,40,50]
mixed = [1,"vanuj","gangrade",True]
print(marks)
print(mixed)
print(marks[2:4])
print(mixed[1:3])
# print(marks,mixed,sep = "\n") just trying something out

mixed.append("VITV")
print(mixed)
clg = mixed.pop()
print(clg)

extra_marks = [60,70,80,90,100]
marks.extend(extra_marks)
print(marks)
marks.insert(1,00)
print(marks)
marks.reverse()
print(marks)

alpha = ["a","b","x","z","p","r","q","w","y"]
alpha.sort(reverse=True)
print(alpha)

#list comprehension
table_of_5 = [5*i for i in range(1,11)]
print(table_of_5)



