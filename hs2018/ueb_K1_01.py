# Umrechnung Sekunden in Jahre
# (c) Martin Guggisberg 2018

eingabe=10**9 ## Eingabe in Sekunden

minute = 60 #Sekunden
stunde = 60 #Minuten
tag = 24 #Stunden
jahr = 365 #Tage

jahr_hat = minute*stunde*tag*jahr # Sekunden

j=eingabe/jahr_hat
print ("10^9 Sekunden sind %g Jahre." % j)

## An welchem Tag kann 10^9 Sekunden gefeiert werden?