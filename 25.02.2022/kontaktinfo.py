def vis_kontaktinfo_foresatt1():
    print("Kontaktinfo foresatt 1")
    print("E-post: mor@epost.no")
    print("Tlf: +47 1291927")

def vis_kontaktinfo_foresatt2():
    print("Kontaktinfo foresatt 2")
    print("E-post: far@epost.no")
    print("Tlf: +47 5326587")

info = input("Hvilken kontakinfo er du interessert i? 1 eller 2. ")
info = int(info)

if info == 1 :
    for tall in range(2):
        print("")
        vis_kontaktinfo_foresatt1()
        print("")

else:
    print("")
    vis_kontaktinfo_foresatt2()
    print("")