#aufgabe 1.5

def fak(n):
    p = 1
    z = 1
    while z < n+1:
        p = p * z
        z = z + 1 
    return p

def summe1(n):
    k = 1
    s = 0.0
    while k < n+1:
        s = s + 1 / fak(k)
        k = k + 1
        print(s)
    return(s)

summe1(20)
    


