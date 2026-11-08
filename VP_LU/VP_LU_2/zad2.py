n = int(input("Enter the number of integers: "))
counter = 0
for i in range(n):
    number = int(input("Enter a number: "))
    counter += number
print(f"The sum is: {counter}")