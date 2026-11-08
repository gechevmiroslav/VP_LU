lower = float(input("Enter the lower limit: "))
upper = float(input("Enter the upper limit: "))
count = 0
for i in range(10):
    number = float(input("Enter a number: "))
    if lower <= number <= upper:
        count += 1
print(f"Count of numbers in the interval: {count}")