my_dict = {"first_one": "можем да го направим"}

def biggest_dict(**kwargs):
    my_dict.update(kwargs)
biggest_dict(name="Ivan", age=20, city="Sofia")

print(my_dict)