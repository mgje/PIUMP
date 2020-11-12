#ueb49.py Newton Verfahren
def ableitung(f,x,h=0.00001): #Ableitung
    res = (f(x+h)-f(x-h))/2.0/h
    return res
#Newton
def newton(f,x0,eps=0.0000000001):
    while abs(f(x0))>eps:
        x0 = x0 - f(x0)/ableitung(f,x0)
    return x0

def poly_f(x):
    return x**5 - 9*x**4 + 33*x**3 - 60*x**2 + 53*x - 19


print ("Newton: Nullstelle der Funktion poly_f : x=%f"%newton(poly_f,0))