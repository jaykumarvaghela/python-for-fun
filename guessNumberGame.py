# import random 
import random

# Create a variable that store random number with some range every ime we load the program 
randNumb = random.randrange(1,201)

# Took user number that the user will guess
guess = int(input("Enter your guess : "))

# Use if and elif condition to match the number. It may be equal, or greater, or lesser.

if(randNumb == guess):
	print("Boom! you Got me. ")
elif(randNumb < guess):
	print("You need to think for LOW")
elif(randNumb > guess):
	print("Can't you think some thing bigger number")
# End of this code.
