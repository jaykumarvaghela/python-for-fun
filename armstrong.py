number = int(input("Enter your number"))

# Main function you can focuse on!


def armstrongNumber(num):
    temp = num
    order = len(str(temp))
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if sum == num:
        print("Its an armstrong number")
    else:
        print("No its not an armstrong number")


# calling main function
armstrongNumber(number)
