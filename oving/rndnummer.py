from random import randint

print("Number generator.")
print("")

randomtall=input("Start?, Yes (yes) or No (no): ")
print("")

while(randomtall !="yes"):
    print("...")
    randomtall=input("Ready? ")
    print("")

print("Generating numbers")
print("")

chosen = randint(0,5)

if chosen == 0:
    tall1 = "0"

elif chosen == 1:
    tall1 = "1"

elif chosen == 2:
    tall1 = "2"

elif chosen == 3:
    tall1 = "3"

elif chosen == 4:
    tall1 = "4"

else: 
    tall1 = "5"

tall1=int(tall1)

print("Your first number is",tall1,".")
print("")


chosen = randint(0,5)

if chosen == 0:
    tall2 = "0"

elif chosen == 1:
    tall2 = "1"

elif chosen == 2:
    tall2 = "2"

elif chosen == 3:
    tall2 = "3"

elif chosen == 4:
    tall2 = "4"

else: 
    tall2 = "5"

tall2=int(tall2)

print("Your second number is",tall2,".")
print("")

if (tall2 == 0):
    print("Unlucky. Try again!")

else:
    number = tall1 + tall2
    print("Your number is",number,"!")
    print("")
