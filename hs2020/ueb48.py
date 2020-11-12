# ueb48 bisektion

def poly_f(x):
    return x**5 - 9*x**4 + 33*x**3 - 60*x**2 + 53*x - 19

# mit wolframalpha anschauen:
# https://www.wolframalpha.com/input/?i=x**5+-+9*x**4+%2B+33*x**3+-+60*x**2+%2B+53*x+-+19

eps = 0.00000001 # kleiner Zahlenwert Epsilon

def bisekt(f,a,b):
    if f(a)*f(b)>0:
        print("kein Vorzeichenwechsel in dem Bereich")
        print("es könnte keine Lösung geben!")
        print("Wählen Sie den Bereich grösser")
        return
    while b-a>eps:
        m = (a+b)/2
        if f(m)*f(a)<=0: # Vorzeichenwechsel zwischen a und m
            b = m        # neues Intervall a..m
        if f(m)*f(b)<=0: # Vorzeichenwechsel zwischen m und b
            a = m        # neues Intervall m..b
    return (a+b)/2

print("Die untersuchte Funktion f(x) hat eine Nullstelle bei x=%f"
      %bisekt(poly_f,-10.0,20.0))