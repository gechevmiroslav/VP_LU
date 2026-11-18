def count_it(sequence):
    numbers = {}

    for digit in sequence:
        digit = int(digit)
        if digit in numbers:
            numbers[digit] += 1
        else:
            numbers[digit] = 1
    sorted_numbers = sorted(numbers, key=numbers.get, reverse=True)

    result = {}
    for digit in sorted_numbers[:3]:
        result[digit] = numbers[digit]
    return result

sequence = input("Enter a sequence of digits: ")

print(count_it(sequence))