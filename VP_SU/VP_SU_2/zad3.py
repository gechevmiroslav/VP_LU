count = int(input("Enter the number of elements: "))
data = {}

for i in range(count):
    key = input("Enter a key: ")
    value = int(input("Enter a value: "))
    data[key] = value
print("Original dictionary:")
for key in data:
    print(key, ":", data[key])

search_key = input("Enter a key to search: ")
if search_key in data:
    print("Value:", data[search_key])
else:
    print("Key not found.")

change_key = input("Enter a key to change: ")
if change_key in data:
    new_value = int(input("Enter the new value: "))
    data[change_key] = new_value
    print("Dictionary after modification:")
    for key in data:
        print(key, ":", data[key])
else:
    print("Key not found.")

delete_key = input("Enter a key to delete: ")
if delete_key in data:
    del data[delete_key]
    print("Dictionary after deletion:")
    for key in data:
        print(key, ":", data[key])
else:
    print("Key not found.")

print("Dictionary keys:")
for key in data:
    print(key)

print("Dictionary values:")
for key in data:
    print(data[key])

sorted_data = dict(sorted(data.items()))
print("Sorted dictionary:")
for key in sorted_data:
    print(key, ":", sorted_data[key])