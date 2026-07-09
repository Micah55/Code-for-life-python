x = int(input("Number 1: "))
y = int(input("Number 2:"))

operation = input("Operation (+/-/*//): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)    
elif operation == "*":
    print(x * y)
elif operation == "/": 
    print(x / y)
else:
    print("Invalid operation")

    

