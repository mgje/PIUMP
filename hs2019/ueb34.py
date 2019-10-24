# ueb 3.4
from math import sqrt

def dist(P,Q):
    return sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)

def laenge(L):
    s = 0
    for i in range(len(L)-1):
        s = s + dist(L[i],L[i+1])
    return s

P1 = [0,0]
P2 = [1,0]
P3 = [1,2]
P4 = [0,2]
pfad = [P1,P2,P3,P4]

print(laenge(pfad))