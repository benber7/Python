from random import randint

player = input ("fire (f), log (l) or water (w)?")

if player == "f":
    print("^^", end="  ")

elif player == "l":
    print("--", end="  ")

elif player == "w":
    print("~~", end="  ")

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = "f"
    print("^^")

elif chosen == 2:
    computer = "l"
    print("--")

else: 
    computer = "w"
    print("~~")

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