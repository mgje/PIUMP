#Uebeung 2.3
#Variablen
v0 = 10
g = 9.81
n = 11
tend = 2*v0/g
dt = tend/n
t = 0
i = 0
# Ausgabe
print("     t      |     y ")
while i<=n:
    y = v0*t-0.5*g*t**2
    print("  %6.2f    |  %6.2f   " % (t,y))
    
    t = t + dt
    i = i + 1




