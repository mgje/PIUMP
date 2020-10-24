from math import sqrt
#ueb4.1 Heronverfahren
def heron(x,epsilon=0.00001):       # Eine Funktion von x und falls angeben epsilon
    a = x                           # Start mit a = x man kann auch a = 1 wählen
    while (a**2-x)**2 > epsilon**2: # Die Bedingung schaut ob die Abweichung zwischen dem Quadrat der Wurzel (a) und der Fläche(x) kleiner epsilon ist
        a = (a + x/a)/2   # Neuer a Wert ist der Mittelwert vom alten a-Wert und x/a 
        ##print(a)        # Interationsschritte ausgeben
    
    return a

# Berechne die Quadratwurzel von 7
print (heron(7)) # Heronberechnung
print (heron(7, 0.0000000001)) # Heronberechnung mit kleinerem epsilon
print (sqrt(7))  # Vergleich mit Bibliothek