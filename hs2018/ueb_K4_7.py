#Uebung 4.7
from math import pi,sin

def mysin(x,n=500):
    res = x
    for k in range(1,n+1):
        res = res * (1-x**2/(k**2*pi**2))
    return res

print(mysin(pi))
print(sin(pi))
    
from gpanel import *
makeGPanel(-6.6, 6.6, -1.2, 1.2)
setColor("gray")
drawGrid(-5.0, 5.0, -1.0, 1.0)
setColor("blue")
lineWidth(2)

x =-5
y = mysin(x)
move(x,y)
while x < 5:
    y = mysin(x)
    draw(x, y)
    x = x + 0.01
