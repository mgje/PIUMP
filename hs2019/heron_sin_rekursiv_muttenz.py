from math import pi,sin
def betrag(x):
    if x < 0:
        x = -x
    return x

def heron(a,x=1.0):
    if betrag(a-x*x) < 0.00000000000001:
        return x
    xneu = (x + a/x)/2
    #print(xneu)
    return heron(a, xneu)

def mysin(x):
    if betrag(x) < 0.0000001:
        return x
    sneu=mysin(x/2)
    return 2*sneu*heron(1-sneu**2)

print (mysin(pi/6)-sin(pi/6))
    
    
