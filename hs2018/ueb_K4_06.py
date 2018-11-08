#uebung K4_6
from math import pi
anz = 5
Z=[z**2 for z in range(1,anz+1)]
N=[z for z in range(1,2*anz,2)]

Z.reverse()  # Reihenfolge der Liste umdrehen
N.reverse()  # Reihenfolge der Liste umdrehen
print(N)
print(Z)

s = 1  
for i in range(len(Z)):
    q = Z[i]/s  # Quotient berechnen
    s = q+N[i]  # Summe berechnen


res = 4/s
print(res)
print(pi)
print("%.17f"%abs(pi-res))

