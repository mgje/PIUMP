#ueb 18
from cmath import *
a = complex(-1,0)
print("Eingabe: a=%.2f +%.2fi"%(a.real,a.imag))
w = phase(a)
r = abs(a)
print("Polar: r= %.2f , w=%.2f"%(r,w))
#Ueberprüfung
z = r* exp(complex(0,w))
print("polar->kartestisch: z=%.2f +%.2fi"%(z.real,z.imag))




print("\n\n")
print(a)
print(z-a)