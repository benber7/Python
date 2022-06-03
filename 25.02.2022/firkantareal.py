def beregn_areal_firkant(lengde, bredde):
    areal = lengde * bredde
    return areal

def er_tall(tekst):
    try:
        float(tekst)
        return True
    except ValueError:
        return False

lengde = float(input("hva er lengden? "))
bredde = float(input("hva er bredden? "))


print(lengde, "*", bredde, "=", beregn_areal_firkant(lengde, bredde))
