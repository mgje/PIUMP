from math import pi
#ueb 4.5

N = 9999999 # grosse Zahl aber nicht unendlich

s = 0.0 # Variable für Summe mit 0 beginnen

for k in range(N):
    s = s + (-1)**k/(2*k+1)
    
# Ausgabe x4 sollte Pi sein
print(4*s)

# Vergleich mit pi
print(pi)

