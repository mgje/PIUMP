from random import randint,choice
from gpanel import *
makeGPanel(0, 500, 0, 500)

## leeres Feld
A = [[0 for i in range(40)] for j in range(40)]
sx = 30
sy = 30
dx = 10

richtung = [[1,0],[0,1],[-1,0],[0,-1]]
indx = -1

x = 20
y = 20

for i in range(9):
    if A[x][y] == 0:
        A[x][y] = 1
        indx = (indx+1)%4
    else:
        A[x][y] = 0
        indx = (indx-1)%4
    x = x + richtung[indx][0]
    y = y + richtung[indx][1]




## Draw
pos = [sx,sy]
for row in A:
    for e in row:
        pos[0] += dx
        move(pos)
        if e == 1:
            fillRectangle(dx, dx)
        
    pos[1] += dx
    pos[0] = sx
    move(pos)
    