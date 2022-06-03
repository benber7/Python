poeng = 0
poeng = int(poeng)

spørsmålliste = ["Hvor mange kontinenter er det?", "Hvor mange stater består USA av?", "Hunder har fire bein", 
"Elon Musk er alien", "Hvor mange planeter er det i melke veien?", "Hvor mange verdens religioner finnes det?"]

print("------------------------------------------------")
print(spørsmålliste[0])
print("------------------------------------------------")
svar1=input("a. Fire (4), b. Fem (5), c. Seks (6), d. Syv (7): ")
print("------------------------------------------------")
print("")

if svar1 == "7":
    print("Du svarte rett!")
    print("")
    poeng = poeng + 1
    print("Du har" , poeng, "poeng")

else:
    print("Du svarte feil!")
    print("")
    poeng = poeng - 1
    print("Du har" , poeng, "poeng")



print("------------------------------------------------")
print(spørsmålliste[1])
print("------------------------------------------------")
svar1=input("a. 50 (50), b. 53 (53), c. 51 (51), d. 48 (48): ")
print("------------------------------------------------")
print("")

if svar1 == "50":
    print("Du svarte rett!")
    print("")
    poeng = poeng + 1
    print("Du har" , poeng, "poeng")


else:
    print("Du svarte feil!")
    print("")
    poeng = poeng - 1
    print("Du har" , poeng, "poeng")


print("------------------------------------------------")
print(spørsmålliste[2])
print("------------------------------------------------")
svar1=input("Ja (ja), Nei (nei): ")
print("------------------------------------------------")
print("")

if svar1 == "ja":
    print("Du svarte rett!")
    print("")
    poeng = poeng + 1
    print("Du har" , poeng, "poeng")


else:
    print("Du svarte feil!")
    print("")
    poeng = poeng - 1
    print("Du har" , poeng, "poeng")


print("------------------------------------------------")
print(spørsmålliste[3])
print("------------------------------------------------")
svar1=input("Ja (ja), Nei (nei): ")
print("------------------------------------------------")
print("")

if svar1 == "ja":
    print("Du svarte rett!")
    print("")
    poeng = poeng+ 1
    print("Du har" , poeng, "poeng")


else:
    print("Du svarte feil!")
    print("")
    poeng = poeng - 1
    print("Du har" , poeng, "poeng")


print("------------------------------------------------")
print(spørsmålliste[4])
print("------------------------------------------------")
svar1=input("a. 700 (700), b. 1 million (1m), c. 100 milliarder (100m): ")
print("------------------------------------------------")
print("")

if svar1 == "700" or "100m":
    print("Du svarte rett!")
    print("")
    poeng = poeng + 1
    print("Du har" , poeng, "poeng")


else:
    print("Du svarte feil!")
    print("")
    poeng = poeng - 1
    print("Du har" , poeng, "poeng")


print("------------------------------------------------")
print(spørsmålliste[5])
print("------------------------------------------------")
svar1=input("a. 5 (5), b. 3 (3), c. 6 (6), d. 4 (4): ")
print("------------------------------------------------")
print("")

if svar1 == "4":
    print("Du svarte rett!")
    print("")
    poeng = poeng + 1
    print("Du har" , poeng, "poeng")


else:
    print("Du svarte feil!")
    print("")
    poeng = poeng - 1
    print("Du har" , poeng, "poeng")

print("")
print("------------------------------------------------")
print("Poengsum:")
print("------------------------------------------------")
print("Du har totalt" , poeng, "poeng")
print("------------------------------------------------")