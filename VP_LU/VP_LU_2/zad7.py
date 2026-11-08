a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
    result = a + b
    print(f"Result: {result}")

elif operation == "-":
    result = a - b
    print(f"Result: {result}")

elif operation == "*":
    result = a * b
    print(f"Result: {result}")

elif operation == "/":
    if b != 0:
        result = a / b
        print(f"Result: {result}")
    else:
        print("Error: 0")