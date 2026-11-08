words = input("Enter words separated by spaces: ").split()
k = int(input("Enter k: "))
result = []
for word in words:
    if len(word) >= k:
        result.append(word)
result = tuple(result)
print("Filtered words:", result)