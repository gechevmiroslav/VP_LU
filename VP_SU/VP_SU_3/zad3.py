def most_valuable(items):
    max_value = 0
    most_valuable_item = ""

    for name in items:
        if items[name] > max_value:
            max_value = items[name]
            most_valuable_item = name
    return most_valuable_item

items = {}
count = int(input("Enter the number of items: "))
for i in range(count):
    name = input("Enter item name: ")
    value = float(input("Enter item value: "))
    items[name] = value

print("Most valuable item:", most_valuable(items))