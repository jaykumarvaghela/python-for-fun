year = int(input())

if year % 400 == 0:
    leap = True

else:
    if year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
