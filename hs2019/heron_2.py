
x = 18
x_i = x

while abs(x_i**2 - x) > 0.05:
    x_i  = (x_i + x/x_i)/2 # neuen x-Wert berechnen
    print(x_i)
