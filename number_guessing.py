# Python Program in Numpy to Guess exact Number between two ranges
import random


lower = int(input("Enter Lower Integer Value:- "))

upper = int(input("Enter Upper Integer Value:- "))


x = random.randint(lower, upper)

number_of_guesses = 6
print("\n\t You've only", number_of_guesses, " chances to guess the integer!\n")


count = 0

while count < number_of_guesses:
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")


if count >= number_of_guesses:
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

