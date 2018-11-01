#Uebung K3.1

def C(F):
    return 5/9*(F-32)

def F(C):
    return 9/5*C+32

res = C(F(0))
print(res)