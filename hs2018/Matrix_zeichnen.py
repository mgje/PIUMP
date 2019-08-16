## Gitter zeichnen

from random import randint,choice
from gpanel import *
## Grafikausgabe
makeGPanel(0, 500, 0, 500)
    
def showMatrix(A):
    sx = 30
    sy = 500-30
    dx = 20
    
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
    
        pos[1] += -dx
        pos[0] = sx
        move(pos)

## Matrix definieren

A = [[1,0,0,0,0],
     [0,1,0,0,0],
     [0,0,1,0,0],
     [0,0,0,1,0],
     [0,0,0,0,1]]
      

    
## Matrix zeichnen
showMatrix(A)



    