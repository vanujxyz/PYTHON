def average(a = 1,b = 20,c = 5):
    avg = (a+b+c)/3
    print(avg)
    return avg #this statement lets me take the result of this function and assign it somewhere


average(10,100,1000) #positional argument

average(2) #a = 2 b = default c = default
average(2,3)#default argument

average(c = 30,a = 10) #keyword argument b taken as default