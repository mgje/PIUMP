#Stammbruchzerlegung
from fractions import gcd
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def kgV(a,b):
    if a > b:
        b,a = a,b
    x = a
    while (x < a*b):
        x = x + a
        if (x % b ==0):
            return x
    return a*b
    
def sub(z1,z2):
    a = z1[0]
    b = z1[1]
    c = z2[0]
    d = z2[1]
    k = lcm(b,d)
    #k = kgV(b,d)
    a2 = a*k//b
    c2 = c*k//d
    a3 = a2-c2
    if a3 < 0:
        a3 = a3 * -1
    return [int(a3),int(k)]

def zerlegung(z):
    #print(z[0]/z[1])
    
    if(z[0]==1):
        return(z)
      
    a = z[0] // gcd(z[0], z[1]) #Kürzen
    b = z[1] // gcd(z[0], z[1])
    z = [a,b]

    l = []
    while (a-1)**2 > 0.01:
        if a == 0:
            break
        z2 = b//a+1
        l.append([1,z2])
        #print(l)
        z = sub(z,[1,z2])
        a = int(z[0])
        b = z[1]
        if b > 10e17: #Abbruch der Zerlegung bei 17 Stellen
            a = 1
    l.append([a,b])
    return l

def test(l):
    s =0.0 
    for e in l:
        s = s + e[0]/e[1]
    return s

print(zerlegung([11,199])) 
#print(zerlegung([67,2012])) 
#print(zerlegung([43538926,64129005])) 
   
        
           
    

