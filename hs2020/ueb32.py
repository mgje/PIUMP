# ueb 3.2

def summe(n):
    s = 0
    k = 1
    while k < n+1:   # Summe mit while Schleife
        s = s + 1.0/k**2
        k = k + 1
    return s

print(summe(23)) # Test mit 23 Summanden

# alternativ

def summe2(n):
    s = 0
    k = 1
    for k in range(1,n+1):   # Summe mit for Schleife
        s = s + 1.0/k**2
    return s

print(summe2(23))# Test mit 23 Summanden