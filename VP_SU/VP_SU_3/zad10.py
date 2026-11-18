def sieve(numbers):
    unique_numbers = set(numbers)
    result = tuple(unique_numbers)
    return result[::-1]

count = int(input("Enter the number of elements: "))
numbers = []
for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Result:", sieve(numbers))