def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation = input("Enter operation (+, -, *, /): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if operation == "+":
    print("Result:", add(a, b))
elif operation == "-":
    print("Result:", subtract(a, b))
elif operation == "*":
    print("Result:", multiply(a, b))
elif operation == "/":
    if a == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", divide(a, b))        
    print("Result:", divide(a, b))
else:
    print("Invalid operation.")