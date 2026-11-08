n = int(input("Enter the number of integers: "))
m = int(input("Enter a number: "))
max_num = m
for i in range(n - 1):
    m = int(input("Enter a number: "))
    if m > max_num:
        max_num = m
print(f"The largest number is: {max_num}")