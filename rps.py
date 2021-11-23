import random
import os

def checkwinner(choice):
	txt = ""
	compchoice = random.choice(["Rock", "Paper", "Scissors"])
	if choice == compchoice:
		txt = "It's a tie!"
	else:
		if choice == "Paper":
			if compchoice == "Rock":
				print("\n\n")
				txt = f"{choice} beats {compchoice}!! You win :D"
			else:
				print("\n\n")
				txt = f"{compchoice} beats {choice}. Better luck next time."
		elif choice == "Scissor":
			print("\n\n")
			if compchoice == "Paper":
				txt = f"{choice} beats {compchoice}!! You win :D"
			else:
				txt = f"{compchoice} beats {choice}. Better luck next time."
		else:
			print("\n\n")
			if compchoice == "Scissor":
				txt = f"{choice} beats {compchoice}!! You win :D"
			else:
				txt = f"{compchoice} beats {choice}. Better luck next time."

	return txt


choicedict = {1: "Rock", 2:"Paper", 3:"Scissos"}
charray = [1,2,3]

play = True

while (play):
	print("\n\n")
	os.system("cls")
	choice = int(input("Let's play some Rock, Paper, Scissors! Enter 1 for Rock, 2 for Paper and 3 for Scissors:"))
	if choice not in charray:
		print("Enter a valid option")
		continue
	else:
		print(checkwinner(choicedict[choice]))
		again = input("Thanks for playing! Hit 'Y' to play again:")
		if again == "Y":
			continue
		else:
			break