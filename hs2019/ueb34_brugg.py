from math import sqrt
# Uebung 3.4
def abstand(L):
    P = L[0]
    Q = L[1]
    z = sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)
    return z


def pfadlaenge(L):
    s = 0
    for i in range(len(L)-1):
        s = s + abstand([L[i],L[i+1]])
    return s
    

l = pfadlaenge([[0,0], [1,0],[1,2], [0,2],[2,3]])
print(l)
