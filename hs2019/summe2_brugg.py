# summe 2

def summe2(n):
    k = 0
    s = 0.0
    while k < n+1:
        s = s + (1/10)**k
        k = k + 1
    return s*9/10
        
        
print(summe2(10))