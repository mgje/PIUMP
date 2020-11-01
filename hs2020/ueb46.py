from math import pi
#ueb46.py Kettenbruch

# 1 + 1^2
#     ---------
#      3+ 2^2
#         --
#          5
#
#
# Rechenschritte mit Speicher s
# s = 5
# s = 2^2/s
# s = s + 3
# s = 1^2/s
# s = s + 1

j = 16
a = 2*j+1 # ungeraden Zahlen im Nenner
b = j+1   # Zähler
s = b**2   # Variable für die Berechnung

while (a > 1):
    s = s + a
    b = b - 1
    s = b**2 / s
    a = a - 2

# noch 1 dazu zählen
s = s + 1.0

p = 4.0 / s

print(p)
print(pi)


    
