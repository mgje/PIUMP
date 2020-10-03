#Uebung 2.1 
print ('------------------')
F = -20                 # Startwert von F
dF = 5                  # Erhöhung pro Durchlauf
while F <= 110:         # Schleifenkopf
    C = (F-32)*5.0/9.0
    print ("f=%.0f \t C=%.2f" % (F, C))          
    F = F + dF          # Schleifenvariable um df erhöhen
print ('------------------')