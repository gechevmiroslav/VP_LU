def find_median(numbers):
    n = len(numbers)

    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    return round(median, 1)

count = int(input("Enter the number of elements: "))
numbers = []
for i in range(count):
    number = float(input("Enter a number: "))
    numbers.append(number)
numbers.sort()

print("Median:", find_median(numbers))