# Anzahl IPV6 Adressen pro m^2
# (c) Martin Guggisberg 2018
from math import *

anz = 2**128 #Anzahl Adressen

r = 6371000 # Radius in Meter
oberflaeche = 4*pi*r**2 #Oberfläche Erde in m^2

pro_m2 = anz/oberflaeche

print("bei einer gleichmässigen Verteilung aller %d Adressen"%anz)
print("gibt es pro Quadratmeter %d Adressen"%pro_m2)