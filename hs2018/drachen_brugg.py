# Drachen
from gturtle import *
from math import sqrt

def drachen(l,s,r):
    if s < 1:
        forward(l)
    else:
        drachen(l/sqrt(2),s-1,1)
        left(r*90)
        drachen(l/sqrt(2),s-1,-1)
makeTurtle()
hideTurtle()
setPos(0,-150)
right(90)
drachen(300,10,1)






