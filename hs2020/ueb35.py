#ueb 3.5
from math import exp,sqrt,pi

def gauss(x,m=0,s=1):
    return 1.0/(sqrt(2*pi)*s)*exp(- (1.0/2)*((x-m)/s)**2)

# tabellarische Ausgabe der Funktionswerte
x = -5
while x < 5.1:
    print("%f \t %f" % (x,gauss(x)))
    x = x + 0.1