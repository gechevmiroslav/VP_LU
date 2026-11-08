day = int(input("Enter a number from 1 to 7: "))
match day:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6:
        name = "Saturday"
    case 7:
        name = "Sunday"
    case _:
        name = "Invalid day"
print(f"Day {day}: {name}")