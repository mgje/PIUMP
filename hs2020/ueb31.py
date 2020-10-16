# ueb 3.1

def C(F):  # Funktion F -> C
    return 5.0/9*(F-32)

def F(C):  # Funktion C -> F
    return 9.0/5*C+32

print(C(F(33))) # Umkehrfunktion testen


liF = range(0,160,10) # Input Liste Fahrenheit von 0 bis 150
loC = [C(x) for x in liF] # Ouput Liste in C für die entsprechenden Inputs

for i in range(len(liF)): # Ausgabe
    print( "%.0fF \t=\t %.0fC" % (liF[i],loC[i]))