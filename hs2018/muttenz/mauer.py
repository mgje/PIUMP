l = [4,2,8,9,1,3,4]
mauer = []

while len(l) > 0:
    mauer.append(l) # Die letzte Zeile der Mauer hinzufügen
    new_l = [] # Initialisiere die neue Zeile
    index = 0 # Setze die Laufvariable auf 0
    while index < (len(l)-1):
        new_value = l[index] + l[index+1] # Den neuen Wert aus der letzten Zeile berechnen
        new_l.append(new_value) # Den neuen Wert unserer neuen Zeile hinzufügen
        index = index + 1 # Die Laufvariable um 1 erhöhen
    l = new_l # Die oberste Zeile der Mauer erstetzen

index = len(mauer)-1
while index >= 0:
    print(mauer[index])
    index = index - 1
