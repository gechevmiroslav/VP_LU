def check_numbers(numbers):
    total = 0

    for number in numbers:
        if number <= total:
            return False
        total += number
    return True

count = int(input("Enter the number of elements: "))
numbers = []
for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

if check_numbers(numbers):
    print("Every number is greater than the sum of the previous numbers.")
else:
    print("The condition is not satisfied.")