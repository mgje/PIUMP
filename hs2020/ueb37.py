#ueb3.7

def ggt_naiv(z1,z2):
    if z1 > z2:     # Falls z1 grösser als z2
        z1,z2 = z2,z1 # Zahlen tauschen
        
    ggT = 1
    for x in range(2,z2):# Probiere alle Zahlen bis zur zweiten Zahl
        if ((z1 % x == 0) and (z2 % x == 0)): #passt der Teiler?
            ggT = x
    return ggT

print(ggt_naiv(907200, 1552320))
        