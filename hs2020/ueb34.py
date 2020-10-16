from math import sqrt
# Uebung 3.4
def abstand(L): # Berechnet den Abstand von Punkten in einer Liste
    P = L[0]
    Q = L[1]
    z = sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)
    return z

def pfadlaenge(L): # Berechnet die Länge eines Pfades definiert durch Punkte in einer Liste
    s = 0
    for i in range(len(L)-1): # Es gibt n-1 Zwischenraeume
        s = s + abstand([L[i],L[i+1]])
    return s

# Definition von Punkte (x,y) 
P1 = [0,0]
P2 = [1,0]
P3 = [1,2]
P4 = [0,2]
pfad = [P1,P2,P3,P4] # Punkte in eine Liste fuellen

l = pfadlaenge(pfad) # Pfadlaenge berechnen
print(l)
