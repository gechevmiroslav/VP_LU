def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    return duplicates

count = int(input("Enter the number of elements: "))
numbers = []
for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Non-unique elements:", find_duplicates(numbers))