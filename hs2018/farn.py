#farn
from math import sqrt
from gturtle import *
from tjaddons import makeRainbowColor

def ast(s,c):
    setPenColor( makeRainbowColor(c) )
    forward(s)
    if s > 4:
        x = getX()
        y = getY()
        hd = heading()
        left(winkel)  
        ast(s*0.67,c+3)
        setPos(x, y)
        heading(hd)
        right(winkel)
        ast(s*0.67,c+3)
        

a = makeTurtle()
hideTurtle()
penWidth(2)
N = 9
L = 160
winkel = 20
setPos(0, -260)
ast(L,0)
