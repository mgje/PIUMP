from math import sin,pi,e

# integration

def integral(f,a,b):
    n = 10000
    delta = (b-a)/n
    s = 0.0
    for i in range(n):
        res = 0.5 * (f(a+i*delta)+f(a+(i+1)*delta))*delta
        s = s + res
    return s
    
def ln(x):
    def u(x):
        return 1.0/x
    return integral(u,1.0,x)

def quad(x):
    return x**2-2*x

#print(integral(quad,1,3))
#print(integral(sin,0,pi))

print(ln(e**5))