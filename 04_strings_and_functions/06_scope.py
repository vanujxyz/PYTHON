x = 10

def square():
    '''this function is used as an example to explain the use of global keyword to modify global variable value'''
    global x
    x = x*x
    return x

square()
print(x) #the value of the global variable changes inside the function using the global keyword
print(square.__doc__)