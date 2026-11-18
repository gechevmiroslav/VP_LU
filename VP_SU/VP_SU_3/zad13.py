def set_gen(numbers):
    result = set()
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
            result.add(str(number) * counts[number])
        else:
            counts[number] = 1
            result.add(number)
    return result

count = int(input("Enter the number of elements: "))
numbers = []
for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Result:", set_gen(numbers))