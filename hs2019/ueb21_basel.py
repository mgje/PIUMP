print ('------------------')
F = 10                   # Startwert von F
dF = 10                  # Erhöhung pro Durchlauf
while F <= 100:          # Schleifenkopf
    C = (5.0/9)*(F - 32)  
    print ("%2.2fF\t %.2fC"%(F, C))          
    F = F + dF          
print ('------------------')