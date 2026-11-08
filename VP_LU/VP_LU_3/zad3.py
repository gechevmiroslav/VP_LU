text = input("Enter a text: ")
result = {}
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)