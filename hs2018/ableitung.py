#Ableitung
from math import sin, pi,log,e,log10


def ableitung(f,x):
    h=0.000001
    res = (f(x+h)-f(x))/h
    return res

def quad(x):
    return x**2-2*x

#print(ableitung(quad,2.0))

print("%.3f"%ableitung(log,1))
print("%.3f"%ableitung(log,0.5))




