# Übung 1.3 
p = -1.0 # Prozent
A = 1000 # Euro
n = 50 # Jahre
E = A*(1+p/100)**n

print ("""Nach %g Jahren 
mit %g%% werden aus dem Kapital %.2f E  
das neue Kapital %.2f E mit einem Ertrag %.2f E"""%(n,p,A,E,E-A))

