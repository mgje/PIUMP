# ueb410 num Ableitung
def quad_f(x):
    return 6*x**2 - 5*x - 19


def diff(f,x,h=0.00001): #Ableitung
    res = (f(x+h)-f(x-h))/2.0/h
    return res

x0 = 5.0/12
print("""Die Ableitung der quadratischen Funktion an der Stelle 5/12 
      ist f'(5/12)=%f"""%diff(quad_f,x0))
   