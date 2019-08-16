from gturtle import *
from random import randint
def dist():
    return sqrt(getX()**2+getY()**2)
def turtleLauf():
    clear()
    setPos(0,0)
    for s in range(1600):
        w = randint(0,359)
        left(w)
        forward(10)
    return dist()
makeTurtle()
hideTurtle()
N=300
s =0
for j in range(N):
    d = turtleLauf()
    s = s + d
print('mitt. Abst.',s/N)

