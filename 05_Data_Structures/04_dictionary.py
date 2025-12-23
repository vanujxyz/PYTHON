marks = {"vanuj" : 8.58,"abdul":7.8,"yash":9.01,"chris":9.91}
print(marks["vanuj"])

marks["vanuj"] = 8.49
print(marks["vanuj"])

print(marks.keys())
print(marks.values())
marks.pop("yash")
print(marks)
marks.clear()
print(marks)

#dictionary comprehension

exp = {x:(x**2,x**3) for x in range(1,11)}
print(exp)

exp2 = {x:tuple([x**i for i in range(2,5)]) for x in range(1,11)} #just trying something
print(exp2)