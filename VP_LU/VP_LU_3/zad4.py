n = int(input("Enter an integer: "))
numbers = list(range(1, n + 1))
reverse_numbers = numbers[::-1]
result = {}
for i in range(len(numbers)):
    result[numbers[i]] = reverse_numbers[i]
print(f"List: {numbers}")
print(f"Dictionary: {result}")