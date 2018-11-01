# Übung K3 04

def laenge(P,Q):
    return sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)

def pfadlaenge(inp):
    s = 0
    for i in range(len(inp)-1):
        w = laenge(inp[i],inp[i+1])
        s = s + w
    return s

pfad = [[0,0],[2,0],[2,1],[0,1]]
laenge = pfadlaenge(pfad)
print(laenge)