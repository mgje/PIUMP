from math import pi
from math import factorial
#ueb47 
x = pi/6.0

#Produktformel
N = 200
p = 1.0
for k in range(1,N+1):
    p = p * (1 - x**2 /k/k/pi/pi)

sx = x*p
print(sx) # sin von pi/6 = sin(30°) = 0.5

#Summenformel sin2.py
N = 4
s = 0.0
for k in range(N+1):
    n = 2*k + 1
    s = s + (-1)**k*x**n/factorial(n)

print(s)
