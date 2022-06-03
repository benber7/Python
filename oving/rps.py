from random import randint

player = input ("rock (r), paper (p) or scissors (s)?")

if player == "r":
    print("O", end="  ")

elif player == "p":
    print("__", end="  ")

elif player == "s":
    print(">8", end="  ")

chosen = randint(1,3)

if chosen == 1:
    computer = "r"
    print("O")

elif chosen == 2:
    computer = "p"
    print("__")

else: 
    computer = "s"
    print(">8")

print (computer)

if player == computer:
    print ("DRAW!")

elif player == "r" and computer == "s":
    print("Player wins!")

elif player == "r" and computer == "p":
    print("Computer wins!")

elif player == "p" and computer == "r":
    print("Player wins!")

elif player == "p" and computer == "s":
    print("Computer wins!")

elif player == "s" and computer == "p":
    print("Player wins!")

elif player == "s" and computer == "r":
    print("Computer wins!")