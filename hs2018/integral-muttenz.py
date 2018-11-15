#integral-Muttenz
from math import e

def integral(f,a,b):
    n = 10000
    delta = (b-a)/n
    s = 0.0
    i = 0
    while i < n:
        res = 0.5 * (f(a+i*delta)+f(a+(i+1)*delta))*delta
        s = s + res
        i = i + 1
    return s

def kehrw(x):
    return 1/x

def quad(x):
    return x*x-2*x

def ln(x):
    res = integral(kehrw,1,x)
    return res

#print(integral(quad,1,3))
#print(quad(1))

print("%.4f"%ln(e**5))