#Program som regner ut strekningen en har kjørt når en vet farten, og hvor lenge en har kjørt.
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("Velkommen til programmet for å regne ut hvor langt du har kjørt!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("")

#La brukeren oppi farten, og lagre dette som en float i variabelen fart
fart = input("Hva var farten på kjøreturen? ")
fart = float(fart)



#La brukeren oppi hvor mange timer en har kjørt, og lagre dette som en float i variabelen tid
tid = input("Hvor lang var kjøreturen i timer? ")
tid = float(tid)


#Lagre om timer en har kjørt er større enn 0 eller ikke i variabelen erTimerOverNull, og skrive ut resultatet
erTimerOverNull = tid > 0


#Viss antall timer kjørt er over 0 regner man ut lengden kjørt, viss ikke skal brukeren få beskjed om at antall timer kjørt må være et tall større enn null
#Dette er eksemepl på bruk av betingelse. (Pcen kjører kode på en betingesle... dette må stemme for at du skal gjøre dette....)
if(erTimerOverNull):
    avstand = fart * tid
    print("Avstanden på kjøreturen er" , avstand, "km!")
else:
    print("Det oppstå et feil. Prøv å bruke tall over 0")