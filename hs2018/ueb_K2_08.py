#Uebeung 2.8 x-Koordinaten

x = 1.0
e = 2.0
dx = 0.05
li = []

while x <= e:
    li.append(x)
    x = x + dx
    # Rundungsfehler vermeiden
    # nach jeder Erhöhung auf 3 Stellen runden
    z = x *1000
    x = round(z)/ 1000 


print(li)
