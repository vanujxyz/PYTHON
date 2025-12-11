vowels = ['a','e','i','o','u']
count = 0
str1 = input("enter your desired string")
for i in str1:
    if i in vowels:
        count += 1
    
print(count)