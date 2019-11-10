from math import sqrt
def abstand(A,B):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    d = sqrt((x2-x1)**2+(y2-y1)**2)
    return d

def szug(kl):
    s = 0
    for i in range(len(kl)-1):
        s = s +abstand(kl[i],kl[i+1])
    return s

l = [[0,0], [1,0],[1,2], [0,2]]
d = szug(l)
print(d)
             