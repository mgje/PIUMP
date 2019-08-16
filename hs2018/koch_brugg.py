# Koch Brugg
from gturtle import *

la = -1
summe = 0

def koch(l,s):
    global la,summe
    if s < 1:
        forward(l)
        la = l
        summe = summe+1
    else:
        koch(l/3,s-1)
        left(60)
        koch(l/3,s-1)
        right(120)
        koch(l/3,s-1)
        left(60)
        koch(l/3,s-1)
    
makeTurtle()
hideTurtle()
setPos(-240,150)
right(90)

koch(500,7)
right(120)

print(summe*la)




