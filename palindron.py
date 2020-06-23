number = int(input("Enter the number:- "))


def palindronFunc(number):
    fNumber = 0
    while number > 0:
        digit = number % 10
        fNumber = fNumber * 10 + digit
        number //= 10
    return fNumber


if number == palindronFunc(number):
    print("Yeah! Its a palindrom.")
else:
    print("No, Its not a palindrom.")
