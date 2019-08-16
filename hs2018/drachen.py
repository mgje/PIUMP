#koch.py
from math import sqrt
from gturtle import *

def drachen(s, n, r):
    if n == 0:
        forward(s)
    else:   
        drachen(s / sqrt(2), n - 1,-1)
        left(r*90)
        drachen(s / sqrt(2), n - 1,1)

a = makeTurtle()
hideTurtle()
N = 9
L = 260
setPos( 0, 0)
left(-90)
drachen(L, N,1)
