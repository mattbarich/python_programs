#guess the number
import random

#Set up Prompt
print("Hello and Welcome to Matts Random Number Guesser!!")
user_name=input("What is your name?: ")
print("Welcome", user_name, "Would you like to play? yes or no")
user_choice = input()
if(user_choice == "no"):
	print("Ok :(( maybe later...")
	exit()
#Guess the number game
else:
	count=int(0)
	lives=int(9)
	lives_left=int(9)
	random_number=random.randint(1,50)
	print(user_name,"I am thinking of a number between 1-50")
	while count <= lives:
		user_number = int(input("Take a guess:"))
		print("Number of Lives left:", lives_left)
		lives_left -= 1
		count += 1
		if user_number == random_number:
			print("You won!!", "Number of tries:", count)
			break
		elif user_number > random_number:
			print("The number im thinking of is lower!")
		elif user_number < random_number:
			print("The number I'm thinking of is higher!")
		if count > lives:
			print("You ran out of lives, you lose :(")
