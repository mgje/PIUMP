#uebung K4_6 Muttenz
# Ohne Liste, Berechnung der Koeffizienten
# mit einer Folge
from math import pi

def skoeff(i):
    return (2*(i-1)+1)

def qkoeff(i):
    return i*i

#print ([skoeff(i) for i in range(1,4)])
#print ([qkoeff(i) for i in range(1,4)])

n = 20
s = 1.0
while n > 0:
    q = qkoeff(n)/s  # Quotient berechnen
    s = skoeff(n)+q  # Summe berechnen
    n = n - 1
    
res = 4/s
print(res)
print(pi)
print("%.17f"%abs(pi-res))