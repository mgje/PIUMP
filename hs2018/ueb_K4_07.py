from math import pi,sin
#uebung 4.7

def mysin(x,N=80):
    p = 1.0
    for k in range(1,N+1):
        p = p * (1- x**2/(k**2*pi**2))
    return x * p
    

alpha = 0.3*pi/2
print("mysin:", mysin(alpha))
print("Vergleich:",sin(alpha))

from gpanel import *
p1 = makeGPanel(-6.2, 6.2, -1.2, 1.2)
title("Graph")
drawGrid(-6.0, 6.0, -1.0, 1.0)

# unbekannte Variable
x = -6
x_max = 6
delta = 0.01
p1.move(x, mysin(x))
p1.setColor("blue")
lineWidth(3)

while x < x_max:
    p1.draw(x, mysin(x,1200))
    x = x + delta
    