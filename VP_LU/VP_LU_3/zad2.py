import random
numbers = [random.randint(1, 100) for _ in range(5)]
print(f"Original list: {numbers}")
result = []
for i in range(len(numbers)):
    result.append(numbers[i])
    if i < len(numbers) - 1:
        result.append(numbers[i] + numbers[i + 1])
print(f"Modified list: {result}")