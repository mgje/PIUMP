#Uebung K4_5
from math import pi

def berechne_pi(anz=10000000):
    s = 0
    for n in range(0,anz+1):
        s = s + (-1)**n/(2*n+1)
        
    return 4*s

print(berechne_pi())
print(pi)