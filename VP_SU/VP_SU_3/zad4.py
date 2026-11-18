def closest_numbers(numbers):
    numbers.sort()
    min_diff = abs(numbers[1] - numbers[0])
    result = [numbers[0], numbers[1]]

    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < min_diff:
            min_diff = diff
            result = [numbers[i], numbers[i + 1]]
    return result

count = int(input("Enter the number of elements: "))
numbers = []
for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Closest numbers:", closest_numbers(numbers))