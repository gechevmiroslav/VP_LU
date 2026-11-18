def find_divisors(number):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

number = int(input("Enter an integer: "))

print("Divisors:", find_divisors(number))