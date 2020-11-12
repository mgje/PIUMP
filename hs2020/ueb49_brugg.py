#ueb4.9
from math import *
def poly_f(x): return x*x*x*x*x-9*x*x*x*x+33*x*x*x-60*x*x+53*x-19
def ableitung(f,x):
    h=0.00001
    return (f(x+h)-f(x-h))/(2*h)
# Newton
# f(x+h)=f(x)+h*f'(x)=0, also h=-f(x)/f'(x)
def newton(f,x0):
    while abs(f(x0))>1e-10:
        x0+=-f(x0)/ableitung(f,x0)
    return x0

print("Newton: Nullstelle von f : x=",newton(poly_f,0))