# ueb 3.2

def summe(n):
    s = 0
    k = 1
    while k < n+1:
        s = s + 1.0/k**2
        k = k + 1
    return s


print(summe(3))