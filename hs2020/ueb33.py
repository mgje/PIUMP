#ueb 3.3
def flaeche(L):
    P1 = L[0]
    P2 = L[1]
    P3 = L[2]  # 0.5 x2y3 - x3y2 - x1y3 + x3y1 + x1y2 - x2y1
    
    A = 0.5 *(P2[0]*P3[1]-P3[0]*P2[1]-P1[0]*P3[1]+ \\
              P3[0]*P1[1]+P1[0]*P2[1]-P2[0]*P1[1])
    return A

A = [0,0]
B = [1,0]
C = [0,2]
L = [A,B,C]

print(flaeche(L))