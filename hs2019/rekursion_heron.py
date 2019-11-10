# heron rekursion

def betrag(x):
    if x < 0:
        x = -1*x
    return x

def heron(a,x=1.0):
    if betrag(a-x*x)<0.00000000001: return x
    xneu=(x+a/x)/2
    return heron(a,xneu)


print("Wurzel aus zwei ist:", heron(2)) 