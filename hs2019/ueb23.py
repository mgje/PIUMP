#ueb23
g = 9.81
t = 0
N = 11
v0 = 20
tot_z = 2*v0/g # 2 Sekunden
dt = tot_z / N

while t <= tot_z:
    y = v0*t - 0.5*g*t**2
    print("h=%.2fm nach t=%.2fs"%(y,t))
    t = t + dt