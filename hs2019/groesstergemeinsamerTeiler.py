# gröster gemeinsamer Teiler

def ggT (z1,z2):
    if z1 > z2:
        z2,z1 = z1,z2
    gT = 1
    for k in range(2,z1+1):
        if (z1 % k == 0) and (z2 % k == 0):
            gT = k
    return gT

print(ggT(45,135))