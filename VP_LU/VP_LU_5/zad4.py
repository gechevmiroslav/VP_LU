def change_list(numbers, value):
    for i in range(len(numbers)):
        if numbers[i] > value:
            numbers[i] = 0

numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

value = int(input("Enter a value: "))
change_list(numbers, value)
print("Modified list:", numbers)