from random import randint,choice
from gpanel import *
makeGPanel(0, 500, 0, 500)

def generate_Matrix(A,x,y,indx):
    if A[x][y] == 0:
        A[x][y] = 1
        indx = (indx+1)%4
    else:
        A[x][y] = 0
        indx = (indx-1)%4
    x = x + richtung[indx][0]
    y = y + richtung[indx][1]
    return A,x,y,indx
    
def showMatrix(A):
    sx = 30
    sy = 30
    dx = 5
    
    ## Draw
    pos = [sx,sy]
    for row in A:
        for e in row:
            pos[0] += dx
            move(pos)
            if e == 1:
                setColor("black")
                fillRectangle(dx, dx)
            else:
                setColor("white")
                fillRectangle(dx, dx)  
        pos[1] += dx
        pos[0] = sx
        move(pos)
  
x = 55
y = 40
## leeres Feld
A = [[0 for i in range(100)] for j in range(100)]
richtung = [[1,0],[0,1],[-1,0],[0,-1]]
indx = -1
    

for j in range(10000):
    A,x,y,indx = generate_Matrix(A,x,y,indx)
    showMatrix(A)

for j in range(1000):
    A,x,y,indx = generate_Matrix(A,x,y,indx)
    showMatrix(A)



    