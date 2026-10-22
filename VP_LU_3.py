print("zad1")
n = int(input("Enter an integer: "))
digits = tuple(int(i) for i in str(abs(n)))
reverse_digits = digits[::-1]
print(f"Forward order: {digits}")
print(f"Reverse order: {reverse_digits}")

print()
print("zad2")
import random
numbers = [random.randint(1, 100) for _ in range(5)]
print(f"Original list: {numbers}")
result = []
for i in range(len(numbers)):
    result.append(numbers[i])
    if i < len(numbers) - 1:
        result.append(numbers[i] + numbers[i + 1])
print(f"Modified list: {result}")

print()
print("zad3")
text = input("Enter a text: ")
result = {}
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)


print()
print("zad4")
n = int(input("Enter an integer: "))
numbers = list(range(1, n + 1))
reverse_numbers = numbers[::-1]
result = {}
for i in range(len(numbers)):
    result[numbers[i]] = reverse_numbers[i]
print(f"List: {numbers}")
print(f"Dictionary: {result}")