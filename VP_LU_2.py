print("zad1")
n = int(input("Enter the number of integers: "))
m = int(input("Enter a number: "))
max_num = m
for i in range(n - 1):
    m = int(input("Enter a number: "))
    if m > max_num:
        max_num = m
print(f"The largest number is: {max_num}")

print()
print("zad2")
n = int(input("Enter the number of integers: "))
counter = 0
for i in range(n):
    number = int(input("Enter a number: "))
    counter += number
print(f"The sum is: {counter}")

print()
print("zad3")
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print("*" * i)

print()
print("zad4")
n = int(input("Enter a number: "))
if n < 2:
    print("The number is not prime.")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")

print()
print("zad5")
day = int(input("Enter a number from 1 to 7: "))
match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6:
        name = "Saturday"
    case 7:
        name = "Sunday"
    case _:
        name = "Invalid day"
print(f"Day {day}: {name}")

print()
print("zad6")
number = float(input("Enter a number: "))
if 1 <= number <= 10:
    print(f"The number {number} is inside the interval [1, 10].")
else:
    print(f"The number {number} is outside the interval [1, 10].")

print()
print("zad7")
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

else:
    print("Invalid operation.")

print()
print("zad8")

print()
print("zad8")
lower = float(input("Enter the lower limit: "))
upper = float(input("Enter the upper limit: "))
count = 0
for i in range(10):
    number = float(input("Enter a number: "))
    if lower <= number <= upper:
        count += 1
print(f"Count of numbers in the interval: {count}")