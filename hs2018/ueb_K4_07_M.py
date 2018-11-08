# Uebung 4.7
from math import pi

def Asin(x,n=10):
    p = x
    k = 1
    while k <= n:
        p = p * (1- x**2/(k**2 * pi**2))
    
    
    return p
    
    
# Aufrufen
print(Asin(pi/6))

