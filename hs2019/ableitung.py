from math import sin,cos,pi

def ableitung2(f,x,h=0.00001):
    return (f(x+h)-f(x-h))/(2*h) 

# Ableitung von sin(60Grad)

w = pi/3
print(ableitung2(sin,w))