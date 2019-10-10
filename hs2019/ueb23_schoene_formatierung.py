#ueb 23
g = 9.81
v0 = 10
N = 10
T = 2*v0/g
dt = T/N
t=0

while t <= T:
    y = v0*t - 0.5*g*t**2
    print("t={:5.2f}\t h= {:5.2f}".format(t,y))
    t = t + dt