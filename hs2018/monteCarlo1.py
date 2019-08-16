from random import randint
def vierMalWuerfeln():
    result = False
    for j in range(4):
        w = randint(1,6)
        if w == 6:
            result = True
    return result
def vierzwanzigMalWuerfeln():
    result = False
    for j in range(24):
        w = randint(1,6)
        q = randint(1,6)
        if w == 6 and q == 6:
            result = True
    return result
def hundertmalSpielen():
    gew = 0
    for i in range(100):
        if vierzwanzigMalWuerfeln():
            gew = gew + 1
    return gew
N = 1000
s = 0.0
for k in range(N):
    a = hundertmalSpielen()
    s = s+a
d = s/N
print('Wahrscheinlichkeit',d/100)
print('Verdienst',d-100*(1-d/100))