""" ROCK, PAPER & SCISSORS by Ravi Teja Gannavarapu """
""" Inspired from Codecademy RPS JavaScript Exercise """

from random import uniform

def userinput():
	choice = raw_input("Do you choose rock, paper or scissors? Type your choice in lower case: ")
	return choice

def compute():
	computerChoice = uniform(0.00, 1.01)
	if (computerChoice < 0.34):
		computerChoice = "rock"
	elif computerChoice <= 0.67:
		computerChoice = "paper"
	else:
		computerChoice = "scissors"
	return computerChoice

def compare(choice1, choice2):
	print ("Computer Choice: " + choice2 + "\n")
	print ("User Choice: " + choice1 + "\n")
	result = ""
	if (choice1 == choice2):
		result = "It's a tie. Try Again!!!"
		print result
		return result
	elif (choice1 == "rock"):
		if (choice2 == "scissors"):
			result = "Rock wins!"
			print result
			return result        
		else:
			result = "Paper wins!"
			print result
			return result
	elif (choice1 == "paper"):
		if (choice2 == "rock"):
			result = "Paper wins!"
			print result
			return result        
		else:
			result = "Scissors wins!"
			print result
			return result
	elif (choice1 == "scissors"):
		if (choice2 == "rock"):
			result = "Rock wins!"
			print result
			return result        
		else:
			result = "Scissors wins!"
			print result
			return result
	else:
			result = "Invalid User Choice!"
			print result
			return result

compare (userinput(), compute())
