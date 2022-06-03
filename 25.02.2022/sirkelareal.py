import math

def beregn_areal_sirkel(radius):
    areal = math.pi * math.pow(radius, 2)
    return areal

radius = float(input("hva er radiusen? "))
print("")

print(math.pi, "*", math.pow(radius, 2), "=", beregn_areal_sirkel(radius))
print("")