#Uebung 2.10 Zahlenmauer

l = [4,2,8,9,1,3,4]
mauer = []

# Zahlenmauer berechnen
while len(l) > 0:
    mauer.append(l)
    nl = []                 # Beginn eine neue Liste
    for i in range(len(l)): # Wiederhole so oft, wie die Liste l lang ist
        if i < len(l)-1:    # Falls nicht der letzte Durchlauf
            nl.append(l[i]+l[i+1]) # Hänge die Summe der beiden Elemente i und i+1 an die Liste nl
    l = nl                  # Nun ist die nächste Reihe fertig gestellt.
    


# Zahlenmauer ausgeben
mauer.reverse() #Drehe die Reihenfolge die Mauer um
tabs = 24       # Leerzeichen für die oberste Reihe
for l in mauer:
    s = '' + tabs*'  '  
    for z in l:
        s = s + ' %3d       '%z
    print s
    tabs = tabs - 3 # 3 Leerzeichen weniger für die nächste Reihe
    
        
    

