
def wurzel(w):
    a = w
    x = 1
    
    for  i in range(10):
        xn = 0.5*(x+a/x)
        x = xn
    return(xn)





print( wurzel(16))