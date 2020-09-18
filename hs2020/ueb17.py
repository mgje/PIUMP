#uebug 1.7

z1 = (2-1j)/(1+1j)
print(z1)

# z2 = a / b

a = complex(sqrt(3),2*sqrt(2))
b = complex(sqrt(3),-1*sqrt(2))
z2 = a/b
print(z2)

a4 = sqrt(3)+2j*sqrt(2)
b4 = sqrt(3)-1j*sqrt(2)
z4 = a4/b4
print(z4)

# z3 = a * b * c / (d*d)
a = 2+1j
b = 3-2j
c = 1+2j
d = 1-1j

z3 = a*b*c/d**2
print(z3) 