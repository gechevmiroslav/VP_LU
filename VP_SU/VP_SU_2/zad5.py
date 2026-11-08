data = {}
for i in range(7):
    key = input("Enter a key: ")
    value = int(input("Enter a value: "))
    data[key] = value

print("Original dictionary:")
for key in data:
    print(key, ":", data[key])

max_key = max(data, key=data.get)
print("Key with maximum value:", max_key)
print("Maximum value:", data[max_key])

change_key = input("Enter a key to change: ")
if change_key in data:
    new_value = int(input("Enter the new value: "))
    data[change_key] = new_value
    print("Dictionary after modification:", data)
else:
    print("Key not found.")

delete_key = input("Enter a key to delete: ")
if delete_key in data:
    del data[delete_key]
    print("Dictionary after deletion:", data)
else:
    print("Key not found.")

new_key = input("Enter a new key: ")
new_value = int(input("Enter a new value: "))
data[new_key] = new_value
print("Dictionary after adding a new element:", data)