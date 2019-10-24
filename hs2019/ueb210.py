# ueb 2.10
l=[4,2,8,9,1,3,4]

while len(l)>1:
    print(l) # Schicht ausgeben
    l2 =[] # Liste auf der nächsten Zeile
    for i in range(len(l)-1): # bis zum zweitletzen Element
        l2.append(l[i]+l[i+1]) # nächste Schicht berechnen
    l = l2 # neue Schicht wird zur l-Schicht

print(l)
    