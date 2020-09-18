# Uebung 1.4
from math import *
g = 2**128 # Anz IPV6 Adressen

r = 6371000 # Erdradius in m
o = 4*pi*r**2 # Oberfläche Erde in m^2
gprom2 = g/o

print("Auf einem 1m^2 könnte man %g IPV6 Adressen vergeben"%gprom2)

nm2 = 10**-9*10**-9
print ("Ein Quadrat nm hat die Fläche %g"%nm2)
gpronm2 = gprom2*nm2
print ("Auf einem nm^2 könnte man %g Adressen vergeben"%gpronm2)
da = 10**-10 # ein Atom hat den Durchmesser von ca. 10^-10 m
print ("Ein Atom hat den Durchmesser von %g m"%da)

print ("Ein Atom nimmt etwa die Oberfläche von %g m2 ein"%da**2)
atpronm2 = nm2/da**2
print ("Auf der Oberfläche von 1nm^2 haben ca. %g Atome Platz."%atpronm2)