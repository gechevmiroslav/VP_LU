contacts = {}
for i in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone nuumber: ")
    contacts[name] = phone
search_name = input("Enter name to search: ")
if search_name in contacts:
    print("Phone number: ", contacts[search_name])
else:
    print("Contact not found.")