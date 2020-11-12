#ueb4.8
def bisekt(f,a,b):
    if f(a)*f(b)>0:
        print("Kein Vorzeichenwechsel–keine Lösung")
        return
    while b-a>0.00001:
        m=(a+b)/2
        if f(m)*f(a)<=0: # Vorzeichenwechsel zw. a und m
            b=m # Neues Intervall a..m
        if f(m)*f(b)<=0: # Vorzeichenwechsel zw. m und b
            a=m
    return (a+b)/2
def fu(x): return x*x*x*x*x - 9*x*x*x*x + 33*x*x*x - 60*x*x + 53*x - 19
print("Bisektionsnullstelle von f : x=",bisekt(fu,0,10))

