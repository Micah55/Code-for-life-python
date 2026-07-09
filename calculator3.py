import math


def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)



def subtraction(x,y):
    total = 0
    total = x - y
    return total

def multiplication(x,y):
    total = 0
    total = x * y
    return total

def division(x,y):
    total = 0
    total = x / y
    return total

def sine(z):
    total = 0
    total = math.sin(z)
    return total

def cosine(z):
    total = 0
    total = math.cos(z)
    return total

def main():
    x = float(input("Number 1:"))
    y = float(input("Number 2:"))
    operation = input("Operation (+/-/*//): ")
    if operation == "+":
        print(addition(x, y))
    elif operation == "-":
        print(subtraction(x, y))
    elif operation == "*":
        print(multiplication(x, y))
    elif operation == "/":
        print(division(x, y))
    else:
        print("Invalid operation")
    z = float(input("Number 3:"))
    operation2 = str(input("Operation2 (sine/cosine): "))
    if operation2 == "sine":
        print(sine(z))
    elif operation2 == "cosine":
        print(cosine(z))
main()


    

