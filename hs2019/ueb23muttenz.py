#ueb 23
g = 9.81
v0 = 15
N = 10
T = 2*v0/g
dt = T/N
t = 0

while t <= T+0.01:
    y = v0*t - 0.5*g*t**2
    print("t=%.2fs \t Höhe %.2fm"%(t,y))
    t = t + dt