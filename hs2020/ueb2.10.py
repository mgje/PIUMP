#ueb 2.10
from math import *
n = 18
x = 1
l = []
N = range(1,n+1,1)
while x <= n:
    y = n/x
    if y in N:
        l.append(x)
        x = x+1
    else:
        x = x+1
print(l)
    