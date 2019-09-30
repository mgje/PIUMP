#ueb 18
from cmath import *
a = complex(-1,0)
w = phase(a)
l = abs(a)
print(l,w)

#Ueberprüfung
z = l* exp(complex(0,w))
print(z)
print(a)
print(z-a)