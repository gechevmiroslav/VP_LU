def palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return 1
    else:
        return 0
number = int(input("Enter a number: "))
print(palindrome(number))