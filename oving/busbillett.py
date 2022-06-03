print("Bussbillett.")
print("")

alder = input("Hvor gammel er du? ")

alder=int(alder)

if (alder < 0):
    print("Negativ tall er ikke gyldig.")

elif (alder <= 5):
    print("Billetten er gartis.")

elif(alder <= 17):
    print("Billetten koster 20kr.")

elif(alder <= 66):
    print("Billetten koster 40kr.")

else:
    print("Billetten kosterr 20kr.")