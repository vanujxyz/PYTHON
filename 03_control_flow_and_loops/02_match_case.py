num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

op = input("+ - * / : ")

match(op):
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case _:
        print("no case matched")

