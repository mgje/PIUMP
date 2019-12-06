from math import log
#integral

def fn(x):
    return 1.0/x

def ftest(x):
    return x

def integral(f,a,b):
    N = 100000
    dx = (b-a)/N
    s = 0.0
    for i in range(N):
        s = s + dx * f(a+i*dx)
    return s


print(integral(fn,1,2))
print(log(2))