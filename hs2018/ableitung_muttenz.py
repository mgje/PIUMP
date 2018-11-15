# ableitung muttenz

def ableitung(f,x):
    h=0.000001
    res = (f(x+h)-f(x))/h
    return res


def quad(x):
    return x**2-2*x



print ("%.4f"%ableitung(quad,2))