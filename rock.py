#Judah Franklin
#Jan 6
#Rock Paper Scissors

#Initialiaze
import random
#Main
print("Welcome to Rock, Paper, Scissors")
#Player making a selection
print("Please seelect either rock paper or scissors: ")
player = input("Selection: ")
Computer = random.randint(1,3)
if Computer == 1:
    Computer = "rock"
elif Computer == 2:
    Computer = "paper"
else:
    Computer = "scissors"
#outcome
if player == "rock" and Computer == "scissors":
    print("Congrats you won")
if player == "rock" and Computer == "paper":
    print("Sorry you lost")
if player == "paper" and Computer == "rock":
    print("Congrats you won")
if player == "paper" and Computer == "scissors":
    print("Sorry you lost")
if player == "scissors" and Computer == "paper":
    print("Congrats you won")
if player == "scissors" and Computer == "rock":
    print("Sorry you lost")
