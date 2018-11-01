#uebung 3.2

def sn(N):
    return sum([1/x**2 for x in range(1,N+1)])

print sn(400)