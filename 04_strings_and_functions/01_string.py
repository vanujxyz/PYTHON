#simple string program

name = "Harry"
print(name)

name2 = 'vanuj'
print(name2)

#multi line string
name3 = '''         
this is
also a string
'''   
print(name3)

#indexing
print(name[0]) #gives H
print(name[1]) #gives A
print(name[-1]) #gives Y , can be thought of like name[len(name) - 1]

#string slicing
print(name2[0:3]) # will print from start to end-1
print(name2[-4:-2])

str1 = "vanujgangrade23bds0282"
print(str1[::2]) #start:stop:step step -> skip x characters 1 means skip nothing to skip n characters we do n+1

#string methods

'''strings are immutable so a statement like name[0] = 'x'  will be wrong '''

'''after using string methods the actual string in memory will not be changed unless explicitly assigned'''

print(len(str1)) #gives the length of string
print(name2.upper()) #gives VANUJ
print(name2.lower()) #gives vanuj
print("hello world".title()) #gives Hello World
print("hello world".capitalize()) #gives Hello world

x = "           vanuj   gangrade            "
print(x)
print(x.rstrip()) #removes the right side whitespaces
print(x.lstrip()) #removes the left side whitespace
print(x.strip()) #removes all excess whitespaces

text = "my name is vanuj gangrade vanuj"

print(text.find('vanuj')) #gives the first occurence of search term
print(text.replace('vanuj','harry')) #replaces all occurences of given term

text2 = "apple,banana,orange"
ls1 = text2.split(',') #returns a list by splitting string based on given term
print(ls1)

print("-".join(ls1)) #returns a string from a list where each item is separated by given term


str2 = "python123"
print(str2.isalpha()) #true if all alphabets
print(str2.isdigit()) #all num
print(str2.isalnum()) #no symbols
print(str2.isspace())

#string formatting and fstrings
print(f"my name is {name2} and my reg no is 23BDS0282 and my cgpa is {8.58:.1f}")
print(f"{name:>10}") #right align
print(f"{name:<10}") #left align
print(f"{name:^10}") #center align