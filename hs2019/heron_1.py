
x = 18
schritte = 5
x_i = x
# Anstatt anz. Schritte so lange, bis x_i^2-x kleiner als 0.05 ist
while schritte > 0:
    x_i  = (x_i + x/x_i)/2 # neuen x-Wert berechnen
    print(x_i)
    schritte = schritte - 1
