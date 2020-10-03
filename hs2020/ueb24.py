#ueb2.4 Berechnung einer Summe
# In diesem Beispiel wird eine Teilsumme der harmonischen 
# Reihe berechnet.

s =0; k=1; M=100
while k <= M:
    s += 1.0 / k
    k = k + 1      # Diese Zeile ist wichtig!
    			   # k wird um 1 erhöht bis k = M ist
    			   # dann endet die Schleife
print(s)
