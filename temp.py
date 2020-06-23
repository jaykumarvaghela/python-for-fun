number = int(input())
numList = []


# while number > 0:
#     digit = int(number % 10)
#     numList.append(digit)
#     number = number / 10


order = len(str(number))
for i in range(1, order+1):
    digit = int(number % 10)
    numList.append(digit)
    number = number / 10
    i += 1

for i in numList:
    power = i ** order
    print(power)
